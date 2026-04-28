# Skills Lab

This lab manages Codex skills through a local-first lifecycle.

## Folder Roles

- `sandbox/`: editable experiments. This is where new skills start.
- `candidates/`: reviewed skills waiting for local production promotion.
- `production/`: approved source copies for local use.
- `evals/`: prompts, observations, and manual test notes.
- `scripts/`: lifecycle automation.

## Commands

Validate a skill:

```text
python3 scripts/validate_skill.py sandbox/<skill-name>
```

Install a sandbox skill locally:

```text
python3 scripts/install_local.py sandbox/<skill-name>
```

Nominate a sandbox skill as a candidate:

```text
python3 scripts/nominate_candidate.py <skill-name>
```

Promote a candidate to local production:

```text
python3 scripts/promote_local.py <skill-name>
```

Prepare a GitHub-safe package:

```text
python3 scripts/prepare_github_release.py <skill-name>
```

## Skill Quality Gates

A skill should not leave `sandbox` until:

- `SKILL.md` exists.
- YAML frontmatter contains `name` and `description`.
- The description makes the trigger conditions clear.
- The body is concise enough for repeated context loading.
- Detailed knowledge is placed in `references/`.
- Repeatable deterministic work is placed in `scripts/`.
- Assets/templates are placed in `assets/`.
- The skill has been tested from Codex on this computer.

Before sharing through GitHub, run a privacy pass:

- Remove secrets, tokens, private URLs, private emails, and credentials.
- Remove hard-coded local paths unless they are examples that must stay local.
- Replace internal company or personal examples with generic versions.
- Confirm scripts do not read private folders by default.
