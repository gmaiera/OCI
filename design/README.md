# OCI Design

OCI Design is the public home for AI-assisted visual work in this toolkit.

Use this area when Codex, Claude, Copilot, Cursor, or another agent needs to make an artifact clearer, more useful, and more visually credible before it leaves the chat.

## This Does That

| If you want to... | Use this | What it does |
|---|---|---|
| Polish an enterprise artifact | [`oracle-design-system`](../Codex/skills/oracle-design-system) | Applies Oracle Redwood-inspired hierarchy, structure, and restraint to pages, apps, dashboards, decks, and stakeholder artifacts. |
| Turn an idea into a webpage | [`export-website`](../Codex/skills/export-website) | Packages a proposal, brief, or workflow into a shareable stakeholder page. |
| Turn an idea into a deck | [`export-pptx`](../Codex/skills/export-pptx) | Creates a concise decision deck for review, alignment, or approval. |
| Prototype a native UI | [Slint](slint/) | Tests a lightweight declarative UI path for visually polished native interfaces. |

## Agent Instructions

For AI-assisted design work:

- Start with the audience and job to be done.
- Prefer real artifact structure over decorative styling.
- Use screenshots, diagrams, charts, or sample UI only when they clarify the decision or workflow.
- Keep public examples generic and reusable.
- Do not publish private transcripts, customer details, internal strategy, local runtime state, credentials, or unapproved drafts.

For Codex, install the full skill collection through the repo plugin and use the runtime skills under [`../Codex/skills`](../Codex/skills).

For Claude, Cursor, Copilot, and other agents, use this folder as the public design brief and route back to the same runtime skill docs rather than duplicating instructions.

## Design Lanes

- **Artifact polish:** webpages, decks, diagrams, executive briefs, approval packets, and reusable stakeholder pages.
- **Design systems:** consistent hierarchy, spacing, interaction patterns, and accessibility checks for enterprise work.
- **Native UI experiments:** Slint samples and smoke tests for small interface prototypes.
- **Visual QA:** browser screenshots, rendered previews, link checks, text-fit checks, and public-safety review before publication.

## Test Fixtures

- [Visual Learning Lab social scheduler test](tests/visual-learning-lab-social-scheduler-test-2026-06-28.md) converts five public-safe learning artifacts into X.com, LinkedIn, and Instagram scheduling drafts.

## Public Safety

This is a public repository. Keep design examples sanitized, generic, and implementation-focused. Do not include private source material, local screenshots that reveal sensitive state, internal URLs, tokens, runtime logs, or machine-specific tool outputs.
