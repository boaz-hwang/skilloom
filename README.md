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
