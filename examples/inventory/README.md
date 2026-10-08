# Preserve requirements before counting lines

[한국어](README.ko.md)

This is an authored, synthetic example of structural refinement and artifact checking. All inputs, instructions, and outputs were written for this repository. No coding agent was run with either instruction file; no human acceptance or performance improvement is claimed. The reference result stands in for an accepted deliverable so you can inspect the workflow without private data.

## Inspect the whole path

1. Reference input: [reference.csv](reference.csv); reference deliverable: [reference-result.json](reference-result.json).
2. The requirements below are fixed before judging the candidate.
3. Compare [baseline instructions](before.md), [candidate instructions](after.md), and the [diff](change.diff).
4. Inspect [new input](new-input.csv), [baseline output fixture](baseline-output.json), and [candidate output fixture](candidate-output.json).
5. Inspect a [regressing output](regression-output.json): the total is still correct, but the zero-stock row disappeared.
6. Run `python3 examples/inventory/check.py` from the repository root. It uses only the Python standard library.

| ID | Requirement | Reference | Baseline fixture | Candidate fixture | Regressing fixture |
| --- | --- | --- | --- | --- | --- |
| R1 | Preserve every row, order, name, quantity, and zero-stock row | Pass | Pass | Pass | Fail |
| R2 | Total equals the sum of source quantities | Pass | Pass | Pass | Pass |
| R3 | JSON items and integer total, with item/integer available entries | Pass | Pass | Pass | Pass |
| R4 | Ask for correction rather than infer missing or invalid input | Not exercised | Not exercised | Not exercised | Not exercised |

The checker verifies R1–R3 on these files and rejects missing names, negative quantities, and non-integer quantities in source data. Rejecting malformed data in Python does **not** prove an agent will ask the right question (R4).

## Recorded local check

On 2026-10-08, `python3 examples/inventory/check.py` passed all fixture expectations, including deliberate omission, quantity, duplicate-row, total, and invalid-input checks. Re-run it to verify the current files. The script exits nonzero on unexpected acceptance or rejection.

## Decision

The shorter instructions remain a **candidate**. Their wording preserves the stated requirements on inspection, and the authored output fixtures pass R1–R3. That does not prove they produce those outputs. Keep the active baseline until actual runs and required human judgments support adoption. Reject the regressing output even though its total is correct.

For an actual trial, run each version in a fresh context on previous-success and new inputs, save the resulting files without overwriting these fixtures, and use `check.py SOURCE.csv OUTPUT.json` to check each artifact. Include invalid-input cases and record whether the agent asks for correction. Fill in the [acceptance record](../../evals/acceptance-record.md), including model, commits, inputs, artifacts, and decisions. Neither speed nor token savings has been measured here.
