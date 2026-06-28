# OCI

OCI helps people turn scattered work into decisions, research, cloud strategy, focused execution, and visually polished stakeholder artifacts.

This repository is a public toolkit for reusable AI-assisted work rituals. It is organized around outcomes: what you want the agent to help you do, and which skill or guide gets you there.

## Start Here

1. **Install the Codex plugin** when you want the full skill collection:

   ```text
   codex plugin marketplace add gmaiera/OCI --ref main --sparse .agents/plugins
   ```

   Then install `OCI Codex Skills` from the Codex plugin marketplace and restart Codex.

2. **Browse by outcome** when you want to understand the toolkit:

   - [Focus](skills/focus/) for priority clarity, visible work, and focused sessions.
   - [Research](skills/research/) for source-backed briefs.
   - [Cloud](skills/cloud/) for architecture, migration, FinOps, and OCI-first technical decisions.
   - [Design](design/) for visual polish, design systems, Slint experiments, artifact QA, and cross-agent instructions.
   - [Artifacts](skills/artifacts/) for webpage and deck export skills.

3. **Read Agent Operations guides** when you want reusable agent-operation practices:

   - [Agent history retention](guides/agent-history-retention.md) explains how to keep local agent history useful without publishing raw transcripts.
   - [Contributing](contributing/) explains how to keep public contributions safe and reviewable.

## This Does That

| If you want to... | Use this | What it does |
|---|---|---|
| Choose what matters right now | [Focus](skills/focus/) | Turns noise into priorities, pipeline visibility, and one useful shipped thing. |
| Understand a topic deeply | [Research](skills/research/) | Produces current, cited, decision-ready research briefs. |
| Make cloud decisions easier | [Cloud](skills/cloud/) | Frames architecture, OCI, migration, FinOps, and provider tradeoffs clearly. |
| Make agent-assisted work more visual | [Design](design/) | Centralizes artifact polish, design-system guidance, Slint tests, and visual QA. |
| Package an idea for others | [Artifacts](skills/artifacts/) | Turns ideas into shareable pages and PPTX decks. |
| Improve agent practice safely | [Agent Operations](guides/) | Documents local-first agent history, privacy, provenance, and reusable patterns. |
| Build or improve a skill | [Lab](lab/) | Explains the sandbox-to-release workflow for Codex skills. |

## Runtime Paths

The visitor-friendly navigation lives in `design/`, `skills/`, `guides/`, `lab/`, and `contributing/`.

The Codex plugin still loads skills from:

```text
Codex/skills
```

For repo-local agent use, the same skill folders are exposed through:

```text
.agents/skills
```

Those compatibility paths stay stable so existing plugin installs and local symlinks keep working.

## Public Safety

This repository is public. Keep contributions generic and reusable. Do not publish credentials, private transcripts, internal strategy, private client or partner details, local runtime state, or unapproved drafts.

Before contributing, review:

- [Security policy](SECURITY.md)
- [Publication checklist](PUBLICATION_CHECKLIST.md)
- [Contribution guide](contributing/)
