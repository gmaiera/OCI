# Plugin-Compatible Codex Skills

This folder is the runtime source for the `oci-codex-skills` plugin bundle.

For visitor-friendly navigation, use [`../../skills`](../../skills). This folder stays organized for Codex compatibility.

## This Does That

| Outcome | Skill | What it does |
|---|---|---|
| Focus | [`now`](now) | Chooses what matters right now. |
| Focus | [`pipeline`](pipeline) | Turns messy work into visible stages, priorities, owners, blockers, and next actions. |
| Focus | [`vibe-work`](vibe-work) | Runs a focused session to ship one useful thing. |
| Research | [`deepresearch`](deepresearch) | Produces current, cited, decision-ready research briefs. |
| Cloud | [`cloud`](cloud) | Frames cloud architecture, migration, FinOps, and OCI-first technical decisions. |
| Artifacts | [`export-website`](export-website) | Turns an idea into a shareable stakeholder webpage. |
| Artifacts | [`export-pptx`](export-pptx) | Turns an idea into a concise decision deck. |
| Artifacts | [`oracle-design-system`](oracle-design-system) | Makes artifacts enterprise-ready and Oracle Redwood-inspired. |

## Install The Full Collection

Add the marketplace from Codex:

```text
codex plugin marketplace add gmaiera/OCI --ref main --sparse .agents/plugins
```

Then install `OCI Codex Skills` from the plugin marketplace and restart Codex. That installs every skill in this folder as one collection.

## Compatibility

Do not rename this folder or move these skill packages without updating and testing:

- [`../../.codex-plugin/plugin.json`](../../.codex-plugin/plugin.json)
- [`../../.agents/plugins/marketplace.json`](../../.agents/plugins/marketplace.json)
- [`../../.agents/skills`](../../.agents/skills)

Skills land here only after they pass the local workflow in [`../skills-lab`](../skills-lab) and a public-safety review.
