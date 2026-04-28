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
| `deepresearch` | Valid | Not public | Medium | Sanitize Gustavo/Oracle-specific framing, then publish as a daily research accelerator. |
| `vibe-work` | Valid | Not public | Medium | Generalize from Gustavo-specific facilitation to team/personal work sessions, then publish. |
| `ludicrous-mode` | Valid, one warning | Not public | Medium | Fix missing reference link, generalize approval language, then publish as an advanced execution mode. |
| `idea-export-v2` | Valid | Not public | Medium/Low | Strong concept, but contains local repo/path and private publishing assumptions. Publish only after a generic version exists. |
| `idea-export` | Valid | Not public | Medium/Low | Older version overlaps with V2. Prefer publishing a cleaned V2 instead of both. |
| `inbox` | Valid | Not public | Low | Keep private. It contains personal email, Oracle/Mesttra/Personal/Affairs routing, and private operating assumptions. |
| `now` | Valid | Not public | Low | Keep private. It depends on Gustavo-specific knowledge sources, lanes, and local priorities. |

## Validation Findings

All current local skills passed structural validation.

One warning was found:

```text
ludicrous-mode: references/execution-log-template.md is not mentioned from SKILL.md
```

That should be fixed before sharing `ludicrous-mode`.

## Privacy Findings

The following skills contain user-specific or organization-specific references:

- `inbox`: personal inbox alias, Oracle, Mesttra, Personal, Affairs, WhatsApp/Slack routing, and private triage assumptions.
- `now`: Gustavo-specific executive-function workflow, Oracle/Mesttra/PF lanes, local knowledgebase/search assumptions.
- `idea-export`: Gustavo-specific publishing flow and local repo paths.
- `idea-export-v2`: Gustavo/Oracle framing and local repo paths.
- `vibe-work`: Gustavo-specific facilitation language.
- `deepresearch`: Gustavo/Oracle-specific opportunity framing.
- `ludicrous-mode`: Gustavo-specific approval language.

These are not necessarily problems for local use. They are reasons to sanitize before publishing.

## Recommended Public Skill Categories

Organize shared skills by daily-work outcomes:

| Category | Purpose | Candidate skills |
|---|---|---|
| Cloud & Architecture | Better technical and commercial cloud decisions | `cloud` |
| Research & Intelligence | Better briefs, market scans, evidence, and citations | `deepresearch` |
| Focus & Execution | Better shipping, autonomy, and completion | `vibe-work`, `ludicrous-mode` |
| Communication & Alignment | Better stakeholder pages, proposals, and calls to action | sanitized `idea-export-v2` |
| Personal Operating Systems | Inbox, prioritization, routines, and command centers | keep private unless rewritten generically |

## Recommended Next Skills To Publish

### 1. `deepresearch`

Why:

- Useful to almost everyone doing technology work.
- Easy to sanitize.
- High daily value for briefs, comparisons, technical decisions, and opportunity scans.

Needed before publishing:

- Remove Gustavo/Oracle-specific framing.
- Replace `latest 2025-2026` with current-date-aware wording.
- Keep the source-quality and citation discipline.

### 2. `vibe-work`

Why:

- Useful for daily productivity and collaborative work.
- Differentiated: it helps people ship one thing instead of just chatting.

Needed before publishing:

- Replace Gustavo-specific language with user/team language.
- Keep the “one session, one challenge, one shipped thing” rule.
- Add a short public README-style usage note in `Codex/skills/README.md`.

### 3. `ludicrous-mode`

Why:

- Powerful for advanced users who want high-autonomy execution.
- Works well as an explicit activation mode.

Needed before publishing:

- Link the execution log template from `SKILL.md`.
- Generalize approval language.
- Keep strict safety boundaries.

### 4. Sanitized `idea-export-v2`

Why:

- Strong for daily stakeholder work.
- Helps people avoid unnecessary slide decks.

Needed before publishing:

- Remove local paths and private repo guidance.
- Replace Gustavo/Oracle language with generic stakeholder language.
- Keep privacy, publishing, and CTA discipline.

## Keep Private For Now

### `inbox`

Keep local because it contains a personal routing system and named lanes. A public version could be created later as `inbox-operator`, but it should be generic and configurable.

### `now`

Keep local because it depends on Gustavo-specific context. A public version could be created later as `priority-briefing`, but it should not assume Oracle, Mesttra, PF, or local notes.

## Recommended Public README Organization

The public `Codex/skills/README.md` should eventually show:

```text
Cloud & Architecture
- cloud

Research & Intelligence
- deepresearch

Focus & Execution
- vibe-work
- ludicrous-mode

Communication & Alignment
- idea-export-v2
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

Keep `cloud` public.

Prepare sanitized public versions next in this order:

1. `deepresearch`
2. `vibe-work`
3. `ludicrous-mode`
4. `idea-export-v2`

