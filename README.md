<h1 align="center">Skilloom</h1>

<p align="center">
  <strong>A loom for agent skills.</strong><br>
  Weave a skill from work you already finished. Keep the threads that hold. Cut the rest.
</p>

<p align="center">
  <a href="README.ko.md">한국어</a> ·
  <a href="#the-four-skills">Skills</a> ·
  <a href="#principles">Principles</a> ·
  <a href="#install">Install</a> ·
  <a href="#for-contributors">Contribute</a>
</p>

<p align="center">
  <a href="https://github.com/boaz-hwang/skilloom/actions/workflows/validate.yml"><img alt="Validate" src="https://github.com/boaz-hwang/skilloom/actions/workflows/validate.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-black.svg"></a>
  <a href="https://github.com/agentskills/agentskills"><img alt="Agent Skills format" src="https://img.shields.io/badge/format-Agent%20Skills-blue.svg"></a>
</p>

---

## Why a loom

A loom holds a few fixed threads, the warp, under tension. Everything else is woven across them.

Skills fail the same way cloth does: not from too little, but from too much. Every fix adds a sentence, every edge case adds a rule, and one day the skill is a wall of instructions that a capable model has to read past to do its job.

Skilloom treats the essential requirements as the warp and leaves the weaving to the model. It starts from evidence you already have, work you accepted, feedback you gave, runs that failed, and keeps only what the result depends on.

## The four skills

Each skill is one motion on the loom. They install and run independently.

| Skill | Motion | Use it to |
| --- | --- | --- |
| [**distill**](skills/distill/README.md) | Spin | Turn a task you just finished and approved into a reusable skill. |
| [**refine**](skills/refine/README.md) | Tighten | Restructure one verbose or overprescriptive skill around its purpose. |
| [**evolve**](skills/evolve/README.md) | Mend | Fix what actually went wrong in use, with the smallest change the evidence supports. |
| [**consolidate**](skills/consolidate/README.md) | Join | Merge overlapping skills without losing any capability that worked. |

Together they cover a skill's whole life: create it from real work, clean it up, repair it from real runs, and fold duplicates back together.

## Principles

These are not slogans. Each one is written into the skills as an instruction.

- **Review deletion first.** Before adding a rule, ask whether removing one would cost an accepted requirement. If not, delete it. Excess is never moved into a reference file to hide it.
- **Trust the model with the how.** Specify the outcome, the decisive constraints, and what done looks like. Leave tools, languages, and implementation choices open.
- **Evidence over intuition.** Accepted deliverables, corrections, and execution records are the input. Missing history is asked for, never invented.
- **Code checks what code can. People judge the rest.** Every generated skill carries its own checks and a short list of human review questions. Counts and formatting never stand in for correctness or taste.
- **Silence is not approval.** The gates that need your confirmation wait for it. The ones that don't are not added.
- **Shorter is not the same as better.** A leaner file is a structural cleanup. A measured improvement needs a comparison under comparable conditions. The skills report which one they did.
- **No change is a valid result.** If the evidence does not support an edit, the skill stays as it is, and the report says why.

## Install

Paste this into your coding agent:

```text
Clone https://github.com/boaz-hwang/skilloom and install each of the four folders under skills/ as a separate skill in your skills directory.
```

Skills follow the [Agent Skills](https://github.com/agentskills/agentskills) format, so they work with any client that reads a `SKILL.md`.

If you installed distill from this repository's root in an earlier version, reinstall it from `skills/distill`.

## Use

Invoke the skill that matches the moment. Each skill's README has a copyable request.

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

## For contributors

The repository ships a format validator and tests. They check structure and Python syntax, never outcome quality; that part is left to the behavioral scenarios in `evals/`, which are run by hand.

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_skill.py skills/distill
python -m unittest discover -s tests -v
```

CI runs the same validation on every push and pull request.

Contributions that make a skill shorter without losing a requirement are welcome. So are contributions that add a requirement the evidence shows was missing. Please bring the evidence.

## License

[MIT](LICENSE)
