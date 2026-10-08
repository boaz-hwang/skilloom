# Real maintenance records and their limits

[한국어](maintenance-records.ko.md)

These are summaries of the author's real maintenance work already published in Skilloom, not new trial results. Public provenance: [initial report, e26e180](https://github.com/boaz-hwang/skilloom/commit/e26e180), [corrected meeting record, 9199860](https://github.com/boaz-hwang/skilloom/commit/9199860). These commits substantiate the published account, not an independently replayable experiment. Private source documents and full execution traces are not included.

## Wiki consolidation: omissions found after shortening

Six skills became five. SKILL.md lines went from 229 to 128, with another 27 lines in two new reference files. Much of the removed material went to shared review references or code. Folder-access failures now failed instead of being counted as zero clippings; an inventory checker covered required sources and item-by-item comparison against the existing wiki, with 12 new tests.

Later comparison found three dropped requirements:

1. Update lost distinctions between proposal and contract, and between training design and current operating rules.
2. Lint no longer checked existence of source paths not yet linked.
3. Ingest no longer had to explain how new evidence changed existing claims.

The 10-clipping cap and fixed claim/page counts were intentionally removed. Intentional removal and unnoticed loss are different decisions. This record does not establish full preservation or better task performance; the line counts are not total package size. It also does not establish that the omitted requirements have since been restored.

## Meeting notes: what was the comparison measuring?

Distill produced a 69-line skill with a 79-line content-check script. Later evolve added guidance to put conclusions and decisions first, mark unsettled diagram structures as drafts, and re-transcribe the full recording with a stronger model when hallucination loops spanned multiple segments. The candidate won its own comparisons, but drifted from an already approved report format. The first two additions were reverted eight minutes later; the re-transcription rule remained.

| Keep these separate | What this record tells us |
| --- | --- |
| Accepted result | An existing report format had already been approved; the private artifact is not published |
| Existing requirements | Preserve the accepted format as well as report content; a complete public requirement inventory is unavailable |
| Change goal | Address feedback from later execution; that feedback did not replace the accepted format |
| Comparison failure | The candidate was judged against same-session feedback rather than the accepted deliverable |
| Decision | Retain the earlier format behavior; keep only the re-transcription addition |

The rollback is evidence that the author rejected the format changes, not evidence that every retained behavior was benchmarked. The lesson for future runs is to name the accepted artifact, preserved requirements, and change goal before comparing. Use the [acceptance record](../evals/acceptance-record.md).
