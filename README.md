<p align="center">
  <img src="assets/skilloom.png" alt="Skilloom" width="480">
</p>

<h1 align="center">Skilloom</h1>

<p align="center">
  <strong>A loom for agent skills.</strong><br>
  Make a skill from work you already finished. Keep only the rules the result depends on. Delete the rest.
</p>

<p align="center">
  <a href="README.ko.md">한국어</a> ·
  <a href="#skills">Skills</a> ·
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

Skills get long. Every fix makes a sentence longer and every edge case adds a rule. Soon a capable model that could handle the job on its own is boxed in by instructions and never gets to show what it can do.

Skilloom starts from work that already succeeded, the deliverable you accepted and the feedback you gave, and keeps only the core. The model decides the rest on its own.

## Used on real work

Before release, these skills ran on the author's own working skills. The numbers below come from git history.

| Skill set | Skilloom skill used | SKILL.md lines | What moved to code | Requirements kept |
| --- | --- | --- | --- | --- |
| Wiki maintenance (6 skills merged into 5) | distill, refine, consolidate | 229 -> 128, plus 27 lines in two new reference files | Clippings folder access errors now fail instead of counting as 0 items. A new script checks the review inventory: required sources, and every item compared with the existing wiki. 12 new tests. | Most. Three were dropped (below). |
| Meeting notes to dashboard | distill, then evolve | New skill: 69, plus a 79-line check script. Evolve: 69 -> 70, then reverted to 69 | Report content checks were in a script from the start | All. Most of the evolve change was reverted (see below). |

Not every removed line was moved. In the wiki set, most went to a shared review reference, the two new reference files, or code checks. Three rules are no longer written down: the update skill's list of things to keep apart was shortened and lost "proposal vs contract" and "training design vs current rule"; the lint skill no longer checks that unlinked source paths exist; and the ingest report no longer has to say how a new source changed existing claims. A 10-item limit per clippings run and fixed targets (3-5 claims, 3-8 pages) were removed on purpose.

For the meeting skill, evolve added rules after later use: put the reader's conclusion and decisions first, label undecided structures as drafts in diagrams, and re-transcribe the whole recording with a stronger model when hallucination loops span several segments. The new version won its own comparison runs. The output had drifted from the report format already approved, though, so the first two rules were reverted 8 minutes later. Only the re-transcription rule stayed. The comparison had measured against feedback from the same session, not against the approved deliverable.

## Skills

Four skills, one for each stage of making and using a skill. Each installs and runs on its own.

| Skill | | Use it to |
| --- | --- | --- |
| [**distill**](skills/distill/README.md) | Spin | Turn a task you just finished and approved into a reusable skill. |
| [**refine**](skills/refine/README.md) | Tighten | Restructure one verbose skill around its purpose. |
| [**evolve**](skills/evolve/README.md) | Mend | Fix what went wrong in use with the smallest change the evidence supports. |
| [**consolidate**](skills/consolidate/README.md) | Join | Merge overlapping skills. Keep the capabilities that worked. |

All four share a few rules.

- Deletion is reviewed before anything is added.
- Code checks what code can check. For the rest, you get a short list of questions and make the call. Whether a table adds up is for code. Whether a sentence reads well is for you.
- A shorter file is not an improvement until it has been compared with the previous version.
- When nothing needs to change, the skill stays as it is. The report says why.

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

The validator and tests check structure and Python syntax only. Outcome quality is checked by hand with the scenarios in `evals/`.

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_skill.py skills/distill
python -m unittest discover -s tests -v
```

CI runs the same checks on every push and pull request. Changes that make a skill shorter are welcome. Keep every requirement, and include the evidence.

## License

[MIT](LICENSE)
