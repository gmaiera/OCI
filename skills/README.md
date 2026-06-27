# OCI Skills

OCI skills are reusable AI work rituals. Each skill answers a simple question: **what should the agent help me do?**

The folders here are a public navigation layer. The Codex plugin runtime source remains under [`../Codex/skills`](../Codex/skills).

## This Does That

| Outcome | Skills | What they do |
|---|---|---|
| [Focus](focus/) | `now`, `pipeline`, `vibe-work` | Choose what matters, organize the work, and ship one useful thing. |
| [Research](research/) | `deepresearch` | Turn uncertainty into current, cited, decision-ready briefs. |
| [Cloud](cloud/) | `cloud` | Make cloud architecture, migration, FinOps, and OCI decisions easier to explain. |
| [Artifacts](artifacts/) | `export-website`, `export-pptx`, `oracle-design-system` | Package ideas into pages, decks, and enterprise-ready visuals. |

## Install

Install the full collection through Codex:

```text
codex plugin marketplace add gmaiera/OCI --ref main --sparse .agents/plugins
```

Then install `OCI Codex Skills` from the plugin marketplace and restart Codex.

## Runtime Source

If you need the actual skill folders, use [`../Codex/skills`](../Codex/skills). That path is kept stable for plugin compatibility.
