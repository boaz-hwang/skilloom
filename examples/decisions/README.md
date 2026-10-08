# When keeping the skill is the result

[한국어](README.ko.md)

## Actual maintenance decision: keep the approved format

In the [meeting-notes record](../maintenance-records.md), most of an evolve change was reverted after it drifted from the approved format. The earlier format behavior was retained, while a separate re-transcription rule stayed. This was a partial rollback, not a complete no-op or a controlled benchmark.

## Reproducible fixture decision: reject a regression

Run `python3 examples/inventory/check.py`. The regressing fixture keeps the correct total but drops the zero-stock row. R1 fails, so reject that output. The shorter instruction candidate stays separate because its actual behavior has not been tested. See the [complete inventory example](../inventory/README.md).

## Authored no-change scenario: service unavailable

[status-case.json](status-case.json) provides an instruction, a mocked successful response, a mocked HTTP 503, and the corresponding output fixtures. The failure response already follows the instruction to report an unverified status. No observed instruction defect supports retries, another service, or a guessed status. The recorded decision is to leave the skill unchanged.

This is an authored decision example, not an observed agent run. The fixture checker verifies only the mock-to-output mapping; it does not establish the quality of an agent's diagnosis. For an actual test, use [evolve scenario 4](../../evals/evolve-scenarios.md) with fresh execution and preserve its transcript and artifacts. Uncertainty about the cause belongs in the report; it does not justify making a change just to produce a diff.
