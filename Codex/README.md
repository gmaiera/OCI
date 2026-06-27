# Codex Runtime Source

This folder holds the Codex-compatible implementation layer for OCI skills.

For first-time visitors, start at the repository root:

- [OCI overview](../README.md)
- [Outcome-based skill navigation](../skills/)
- [Guides](../guides/)

## What This Folder Does

| Path | This does that |
|---|---|
| [`skills`](skills) | Holds the public skill packages loaded by the Codex plugin. |
| [`skills-lab`](skills-lab) | Holds sandbox, candidate, production, eval, and release workflows for skill development. |
| [`WORKFLOW.md`](WORKFLOW.md) | Shows how the skills combine into an organization-wide work-improvement loop. |
| [`SYSTEM_CHECK.md`](SYSTEM_CHECK.md) | Records the public skill inventory and shareability review. |
| [`plans`](plans) | Holds implementation-plan pointers; broadly useful plans graduate into `../guides`. |

## Runtime Contract

The Codex plugin bundle loads from:

```text
Codex/skills
```

Repo-local agents also see those skills through:

```text
.agents/skills
```

Keep those compatibility paths stable unless the plugin metadata, symlinks, and installation docs are updated and tested together.

## Skill Lifecycle

Skills move through this path:

```text
skills-lab/sandbox
  -> skills-lab/candidates
  -> skills-lab/production
  -> skills
```

Only `skills/` is intended as the plugin-compatible public release source. Treat `skills-lab/` as working material unless a release review explicitly promotes content.
