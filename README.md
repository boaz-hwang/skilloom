<p align="center">
  <img src="assets/skilloom.png" alt="Skilloom" width="480">
</p>

<h1 align="center">Skilloom</h1>

<p align="center">
  <strong>Turn work you approved into skills you can trust.</strong><br>
  Capture what made the result work. Refine, repair, and merge skills while checking that those requirements still hold.
</p>

<p align="center">
  <a href="README.ko.md">한국어</a> ·
  <a href="#choose-the-change-you-need">Skills</a> ·
  <a href="#install">Install</a> ·
  <a href="#use">Use</a> ·
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <a href="https://github.com/boaz-hwang/skilloom/actions/workflows/validate.yml"><img alt="Validate" src="https://github.com/boaz-hwang/skilloom/actions/workflows/validate.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-black.svg"></a>
  <a href="https://github.com/agentskills/agentskills"><img alt="Agent Skills format" src="https://img.shields.io/badge/format-Agent%20Skills-blue.svg"></a>
</p>

---

Skilloom starts with a deliverable you accepted and the feedback that made it right. It helps you turn that experience into a reusable skill, then maintain the requirements as the skill changes. Shorter instructions are useful only when they still support the intended result.

## Choose the change you need

Four independent skills. Pick one for the change in front of you; they are not a sequence you need to run.

| Your situation | Skill | Scope |
| --- | --- | --- |
| You want to reproduce work you finished and approved | [**distill**](skills/distill/README.md) | Create a new skill from the accepted result and corrections |
| One skill needs clearer structure and fewer unnecessary instructions | [**refine**](skills/refine/README.md) | Restructure the whole skill while preserving essential requirements |
| Actual use exposed a specific problem | [**evolve**](skills/evolve/README.md) | Make the smallest change supported by execution evidence |
| Several skills overlap | [**consolidate**](skills/consolidate/README.md) | Merge suitable roles while retaining their useful capabilities |

Refine and evolve differ in the **scope of change**, not simply in whether logs exist. Refine may reorganize the whole skill. Evolve stays with the observed problem; a broader rewrite belongs in a separate refinement task.

All four share a few rules:

- Review deletion before adding instructions. Keep non-obvious knowledge and essential exceptions.
- Let code check objective requirements; leave concrete quality questions to the person who uses the result.
- Compare against the original requirements. Fewer lines alone do not establish improvement.
- Keep the existing skill when no useful change is supported. An unconfirmed candidate stays separate.

## Where Skilloom fits

Use Skilloom when you already work with an agent that reads `SKILL.md`, want to carry accepted work into future tasks, and want control over how much an existing skill changes. Each skill installs independently; no separate optimization service is required. Generated skills may still need task-specific tools and checks.

Other projects address related parts of this problem. These are differences in workflow, not comparative performance claims (documentation reviewed 2026-10-08).

| Project | Focus in its documentation | Skilloom's emphasis |
| --- | --- | --- |
| [Claudeception](https://github.com/blader/Claudeception) | Extract reusable discoveries from work sessions, with optional hooks | Start distillation from an accepted deliverable and the user's corrections |
| [Anthropic skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Create and improve skills with evaluations and description optimization | Separate whole-skill refinement, localized repair, and multi-skill consolidation |
| [SkillHone](https://github.com/Tencent/SkillHone) | Repair complete skill repositories with regression tests, decision history, and local PRs | Four independently invoked skills operating in your existing agent session |
| [EvoSkill](https://github.com/sentient-agi/EvoSkill) | Automate skill and prompt evolution using benchmarks and held-out evaluation | Start from supplied work and feedback; scale verification to the change |
| [SkillX](https://github.com/zjunlp/SkillX) | Extract, filter, merge, and expand a hierarchical skill knowledge base | Review a supplied set of skills and confirm the concrete consolidation mapping |

Human review, evaluation, and skill extraction also exist elsewhere. Skilloom's proposed value is their combination with accepted-result grounding, deletion-first review, and bounded changes. Whether that improves your work needs evidence from your tasks.

## Inspect the evidence

**Start with the [reproducible inventory example](examples/inventory/README.md).** It includes a reference result, requirements, before/after instructions, new input, output fixtures, a diff, and an executable checker. It demonstrates checking requirements independently of instruction length, including rejecting an output whose total is correct but whose rows are incomplete. It is an authored example, not an agent benchmark or a user-approved production run.

```bash
python3 examples/inventory/check.py
```

The example also records a **retain-baseline decision** when a candidate omits a zero-stock row, and a **no-change decision** when a service failure is already handled correctly. See [when retaining the skill is the result](examples/decisions/README.md).

### Real maintenance records

These records come from the author's own work. The public summaries do not include private source documents or complete execution traces, so they are not independently reproducible benchmarks.

| Case | Observed result | What it establishes |
| --- | --- | --- |
| Wiki maintenance: 6 skills merged into 5; SKILL.md lines 229 → 128, plus 27 lines in two new reference files | Later comparison found three dropped requirements | A shorter set can still lose requirements. This is an omission-detection case, not proof of successful compression. |
| Meeting notes: an evolve candidate won its own comparisons, then most changes were reverted 8 minutes later | The output had drifted from the approved report format; the re-transcription rule remained | The comparison target matters. A local win did not establish preservation of the accepted result. |

Read the [case details and limits](examples/maintenance-records.md), including what was removed intentionally and what remains unverified.

For your own comparison, use the [acceptance record](evals/acceptance-record.md) to separate the accepted result, existing requirements, and the goal of this change **before** evaluating candidates. A format pass, a model's self-rating, and human acceptance are different kinds of evidence.

## Install

Paste this into your coding agent:

```text
Clone https://github.com/boaz-hwang/skilloom and install each of the four folders under skills/ as a separate skill in your skills directory.
```

Skills follow the [Agent Skills](https://github.com/agentskills/agentskills) format. They work with any client that reads a `SKILL.md`.

If you installed distill from this repository's root in an earlier version, reinstall it from `skills/distill`.

## Use

Call the skill that fits the moment. Each skill's README has a copyable request.

```text
Use distill to turn this task into a reusable skill.
```

```text
Use refine to restructure <skill-name> around its purpose and essential requirements.
```

```text
Use evolve to review <skill-name>'s execution records and make the smallest improvements they support.
```

```text
Use consolidate to review <skill-folder>, propose suitable merges, and consolidate after I confirm the plan.
```

Recommended models:

- Fable 5.1
- Astra 6

## Contributing

The package validator and existing unit tests check structure and Python syntax. The inventory example checks its explicit fixture requirements; neither establishes agent performance. Evaluate actual skill behavior with the scenarios in `evals/`, keeping run evidence in an acceptance record.

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_skill.py skills/distill
python -m unittest discover -s tests -v
```

CI runs package checks and the inventory fixture check on every push and pull request. Changes that make a skill clearer or smaller are welcome when requirements are preserved. Include the evidence; a justified no-change decision is also a useful evaluation result.

## License

[MIT](LICENSE)
