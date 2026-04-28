# Codex Skills System Check

Date: 2026-04-28

## Current Goal

Make `https://github.com/gmaiera/OCI` easy for people to browse so they can open `Codex/skills`, find useful daily-work skills, and copy the skill folders into their own Codex setup.

## Public Structure

```text
Codex/
├── README.md
├── SYSTEM_CHECK.md
├── skills/
│   ├── README.md
│   └── cloud/
└── skills-lab/
    ├── README.md
    ├── registry.yaml
    ├── sandbox/
    ├── candidates/
    ├── production/
    ├── evals/
    └── scripts/
```

## Skill Inventory

| Skill | Local status | Public status | Shareability | Recommendation |
|---|---|---|---|---|
| `cloud` | Valid | Published in `Codex/skills/cloud` | High | Keep public. Strong first shared skill for OCI/cloud work. |
| `deepresearch` | Valid | Published in `Codex/skills/deepresearch` | High | Public sanitized version implemented. |
| `pipeline` | New public skill | Published in `Codex/skills/pipeline` | High | Public skill implemented for daily work organization. |
| `vibe-work` | Valid | Published in `Codex/skills/vibe-work` | High | Public sanitized version implemented. |
| `ludicrous-mode` | Valid, one warning | Not public | Medium | Fix missing reference link, generalize approval language, then publish as an advanced execution mode. |
| `idea-export-v2` | Valid | Not public | Low | Do not publish. User chose V1 `idea-export` without V2. |
| `idea-export` | Valid | Published in `Codex/skills/idea-export` | High | Public sanitized V1 implemented. |
| `inbox` | Valid | Not public | Low | Keep private. It contains personal inbox routing, named work/life lanes, and private operating assumptions. |
| `now` | Valid | Published in `Codex/skills/now` | High | Public sanitized version implemented. Keep private local variant separate. |

## Validation Findings

All current local skills passed structural validation.

One warning was found:

```text
ludicrous-mode: references/execution-log-template.md is not mentioned from SKILL.md
```

That should be fixed before sharing `ludicrous-mode`.

## Privacy Findings

The following skills contain user-specific or organization-specific references:

- `inbox`: personal inbox alias, named work/life lanes, channel routing, and private triage assumptions.
- `now`: user-specific executive-function workflow, private work/life lanes, local knowledgebase/search assumptions.
- `idea-export`: user-specific publishing flow and local repo paths.
- `idea-export-v2`: user/company-specific framing and local repo paths.
- `vibe-work`: user-specific facilitation language.
- `deepresearch`: user/company-specific opportunity framing.
- `ludicrous-mode`: user-specific approval language.

These are not necessarily problems for local use. They are reasons to sanitize before publishing.

## Recommended Public Skill Categories

Organize shared skills by daily-work outcomes:

| Category | Purpose | Candidate skills |
|---|---|---|
| Cloud & Architecture | Better technical and commercial cloud decisions | `cloud` |
| Research & Intelligence | Better briefs, market scans, evidence, and citations | `deepresearch` |
| Focus & Execution | Better shipping, autonomy, and completion | `vibe-work`, `ludicrous-mode` |
| Communication & Alignment | Better stakeholder pages, proposals, and calls to action | `idea-export` |
| Personal Operating Systems | Inbox, prioritization, routines, and command centers | keep private unless rewritten generically |

## Recommended Next Skills To Publish

### 1. `ludicrous-mode`

Why:

- Powerful for advanced users who want high-autonomy execution.
- Works well as an explicit activation mode.

Needed before publishing:

- Link the execution log template from `SKILL.md`.
- Generalize approval language.
- Keep strict safety boundaries.

No additional daily-work skills are queued for publishing in this batch.

## Keep Private For Now

### `inbox`

Keep local because it contains a personal routing system and named lanes. A public version could be created later as `inbox-operator`, but it should be generic and configurable.

### `now`

Keep local because it depends on user-specific context. A public version could be created later as `priority-briefing`, but it should not assume private work/life lanes or local notes.

## Recommended Public README Organization

The public `Codex/skills/README.md` should eventually show:

```text
Cloud & Architecture
- cloud

Research & Intelligence
- deepresearch

Focus & Execution
- pipeline
- now
- vibe-work

Communication & Alignment
- idea-export
```

Each listed skill should include:

- What it helps with.
- When to use it.
- Copy/install instruction.
- Safety or privacy note when relevant.

## Release Gates

Before any skill enters `Codex/skills`:

1. It must pass `validate_skill.py`.
2. It must have `SKILL.md`.
3. It should have `agents/openai.yaml`.
4. It must pass the privacy scan in `prepare_github_release.py`.
5. It must be tested locally from `~/.codex/skills`.
6. It should have at least one eval prompt file under `skills-lab/evals/<skill-name>/prompts.md`.
7. It must not contain private emails, tokens, local paths, internal-only context, or personal operating assumptions.

## Current Decision

Keep these skills public:

1. `cloud`
2. `deepresearch`
3. `pipeline`
4. `now`
5. `vibe-work`
6. `idea-export`

Do not publish `idea-export-v2` in this repository. Keep it private unless a future decision explicitly revives it.
