# Codex Skills System Check

Date: 2026-04-28

## Current Goal

Keep `https://github.com/gmaiera/OCI` easy to browse while sharing only the Codex skills that are ready for public use. Internal-only modes and personal operating workflows should stay outside the public repo until they are deliberately rewritten, reviewed, and approved for sharing.

## Actual Public Structure

```text
Codex/
├── README.md
├── SYSTEM_CHECK.md
├── WORKFLOW.md
├── skills/
│   ├── README.md
│   ├── cloud/
│   ├── deepresearch/
│   ├── now/
│   ├── oracle-design-system/
│   ├── pipeline/
│   └── vibe-work/
└── skills-lab/
    ├── README.md
    ├── registry.yaml
    ├── sandbox/
    ├── candidates/
    ├── production/
    ├── evals/
    └── scripts/
```

## Public Skill Inventory

| Skill | Public status | Shareability | Decision |
|---|---|---|---|
| `cloud` | Published in `Codex/skills/cloud` | High | Keep public. Strong shared skill for OCI, multi-cloud architecture, migration, and FinOps work. |
| `deepresearch` | Published in `Codex/skills/deepresearch` | High | Keep public. Useful for rigorous, source-backed research briefs. |
| `pipeline` | Published in `Codex/skills/pipeline` | High | Keep public. Useful for daily work organization and flow review. |
| `now` | Published in `Codex/skills/now` | High | Keep public sanitized version. Keep private local variants separate. |
| `vibe-work` | Published in `Codex/skills/vibe-work` | High | Keep public sanitized version. Useful for focused work sessions. |
| `oracle-design-system` | Published in `Codex/skills/oracle-design-system` | High | Keep public. Useful for Oracle Redwood-inspired design consistency. |

## Internal Or Removed Work

| Area | Public decision | Reason |
|---|---|---|
| Advanced execution modes | Keep internal only. Do not list as public candidates. | These should be worked privately before any future public decision. |
| Communication packaging experiments | Removed from public repo. | These flows are not part of the current public sharing plan. |
| Personal inbox workflows | Keep internal only. | These depend on private routing, named work/life lanes, and triage assumptions. |

## Validation Findings

Current public skills should be validated before each release with:

```text
python3 skills-lab/scripts/validate_skill.py skills/<skill-name>
```

There are no validation items for internal-only modes or removed communication packaging experiments because they are no longer part of the public repo.

## Privacy Findings

Public skills must not contain private emails, tokens, local paths, internal-only context, or personal operating assumptions.

Current privacy posture:

- `cloud`, `deepresearch`, `pipeline`, `vibe-work`, and `oracle-design-system` are intended as generic public skills.
- `now` is public only in sanitized form. Any local version with private knowledgebase assumptions should remain internal.
- Advanced execution modes, personal inbox workflows, and retired communication packaging experiments should stay out of the public repo.

## Recommended Public Skill Categories

Organize shared skills by daily-work outcomes:

| Category | Purpose | Public skills |
|---|---|---|
| Cloud & Architecture | Better technical and commercial cloud decisions | `cloud` |
| Research & Intelligence | Better briefs, market scans, evidence, and citations | `deepresearch` |
| Focus & Execution | Better prioritization, flow, shipping, and completion | `now`, `pipeline`, `vibe-work` |
| Communication & Alignment | Better design consistency for shared artifacts | `oracle-design-system` |

## Recommended Public README Organization

The public `Codex/skills/README.md` should show only currently published public skills:

```text
Cloud & Architecture
- cloud

Research & Intelligence
- deepresearch

Focus & Execution
- now
- pipeline
- vibe-work

Communication & Alignment
- oracle-design-system
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
6. `oracle-design-system`

Keep internal-only modes and personal workflows out of this public inventory unless a future review explicitly approves a generic public version.
