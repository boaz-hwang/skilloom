"""Check authored artifacts, not agent performance. Uses Python's standard library."""
import copy
import csv
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent


def read_source(path):
    with path.open(newline='', encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ['item', 'available']:
            raise ValueError('Expected item,available CSV columns')
        rows = []
        for row in reader:
            name, quantity = row['item'], row['available']
            if (None in row or not name or not name.strip() or quantity is None
                    or re.fullmatch(r'[0-9]+', quantity) is None):
                raise ValueError('Missing name or invalid nonnegative integer quantity')
            rows.append({'item': name, 'available': int(quantity)})
        return rows


def check(rows, output):
    schema = (isinstance(output, dict) and set(output) == {'items', 'total'}
              and isinstance(output['items'], list) and type(output['total']) is int
              and all(isinstance(row, dict) and set(row) == {'item', 'available'}
                      and isinstance(row['item'], str) and type(row['available']) is int
                      for row in output['items']))
    if not schema:
        return ['R3']
    failures = []
    if output['items'] != rows:
        failures.append('R1')
    if output['total'] != sum(row['available'] for row in rows):
        failures.append('R2')
    return failures


def fixture_checks():
    import tempfile
    cases = [
        ('reference.csv', 'reference-result.json', []),
        ('new-input.csv', 'baseline-output.json', []),
        ('new-input.csv', 'candidate-output.json', []),
        ('new-input.csv', 'regression-output.json', ['R1']),
    ]
    for source, artifact, expected in cases:
        actual = check(read_source(HERE / source), json.loads((HERE / artifact).read_text()))
        if actual != expected:
            raise ValueError(f'{artifact}: expected {expected}, got {actual}')
        print(f'{artifact}: {"PASS" if not actual else "REJECT " + ", ".join(actual)} (expected)')

    rows = read_source(HERE / 'new-input.csv')
    good = json.loads((HERE / 'candidate-output.json').read_text())
    # A correct total alone must not hide changed data, missing rows, or duplicates.
    for name in ['quantity', 'duplicate', 'order', 'total', 'boolean']:
        bad = copy.deepcopy(good)
        expected = ['R1']
        if name == 'quantity':
            bad['items'][1]['available'] += 1
        elif name == 'duplicate':
            bad['items'].append(copy.deepcopy(bad['items'][0]))
        elif name == 'order':
            bad['items'].reverse()
        elif name == 'total':
            bad['total'] += 1
            expected = ['R2']
        else:
            bad['items'][0]['available'] = False
            expected = ['R3']
        if check(rows, bad) != expected:
            raise ValueError(f'Checker failed to identify {name} defect')
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / 'invalid.csv'
        for row in [',1', 'clips,', 'clips,-1', 'clips,1.5', 'clips,abc', 'clips,1,extra']:
            path.write_text('item,available\n' + row + '\n')
            try:
                read_source(path)
            except ValueError:
                continue
            raise ValueError(f'Checker accepted invalid input: {row}')
    status = json.loads((HERE.parent / 'decisions/status-case.json').read_text())
    for case in status['cases']:
        expected = ('Service status: ' + case['body']['status'] + '.'
                    if case['http_status'] == 200 else 'Service status could not be verified.')
        if case['output'] != expected:
            raise ValueError('Status output does not match the declared mock response')
    if status['decision'] != 'no change':
        raise ValueError('Authored no-change decision was altered')
    print('Defect checks and status fixture mapping: PASS')
    print('Scope: authored artifacts only; agent behavior and human acceptance NOT tested.')


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            fixture_checks()
        elif len(sys.argv) == 3:
            failures = check(read_source(Path(sys.argv[1])), json.loads(Path(sys.argv[2]).read_text()))
            print('REJECT: ' + ', '.join(failures) if failures else 'PASS: R1–R3 only; R4 and agent performance untested')
            sys.exit(1 if failures else 0)
        else:
            raise ValueError('Usage: check.py [SOURCE.csv OUTPUT.json]')
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
