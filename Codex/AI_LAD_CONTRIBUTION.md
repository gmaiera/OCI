# AI LAD Skills Contribution

Date: 2026-04-28

## Target

Oracle AI LAD skills site:

```text
https://ai-lad.com/skills
```

The target URL is protected by Oracle IDCS SSO and is not a Git remote. Contribution requires authenticated browser access or the underlying repository clone URL.

## Contribution Package

The GitHub-safe contribution source is:

```text
Codex/skills
```

It contains eight validated, sanitized Codex skills intended for shared team use:

| Skill | Purpose |
|---|---|
| `cloud` | Cloud architecture, migration, workload sizing, cost comparison, FinOps, Well-Architected review, and OCI-first enterprise recommendations. |
| `deepresearch` | Current, source-backed, multi-phase research briefs for technical, market, company, person, or opportunity analysis. |
| `pipeline` | Work intake and flow review across priorities, stages, owners, blockers, and next actions. |
| `now` | Near-term prioritization and focus selection from available context. |
| `vibe-work` | Focused "ship one thing" work sessions for individuals or small groups. |
| `export-website` | Stakeholder-ready shareable webpages for proposals, ideas, briefs, and alignment. |
| `export-pptx` | Concise PowerPoint decision decks with storyline, proof, and next-step framing. |
| `oracle-design-system` | Oracle Redwood-inspired design polish for webpages, apps, decks, and stakeholder artifacts. |

## Validation

Validation command run from `Codex/`:

```text
for s in cloud deepresearch export-website export-pptx pipeline now vibe-work oracle-design-system; do python3 skills-lab/scripts/validate_skill.py skills/$s || exit 1; done
```

Result:

```text
PASSED
PASSED
PASSED
PASSED
PASSED
PASSED
PASSED
PASSED
```

## Privacy Posture

The public packages under `Codex/skills` are intended to be generic and shareable. Internal-only modes, personal inbox workflows, private knowledgebase assumptions, local machine paths, and personal routing details are intentionally excluded.

Before submitting to the Oracle AI LAD repository, do one final review of:

- `Codex/skills/README.md`
- `Codex/SYSTEM_CHECK.md`
- Each `Codex/skills/<skill-name>/SKILL.md`

## Submission Options

If the Oracle AI LAD site supports direct upload, submit the folders under `Codex/skills`.

If there is an underlying Git repository, clone it separately and copy these folders into the repository's expected skills location. Keep the local source of truth in this repo unless the Oracle repository defines a stricter package format.

Required missing input:

```text
Authenticated AI LAD contribution instructions or repository clone URL.
```
