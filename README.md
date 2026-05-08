# OCI

A living collection of OCI ideas, skills, workflows, and experiments I am excited to share because they help turn important work into something others can use.

## Public Codex Skills

The public Codex skills are in:

```text
Codex/skills
```

The repo is also published as a Codex plugin bundle named `oci-codex-skills`, so the full collection can be installed together instead of selecting one skill folder at a time.

To add the marketplace from Codex:

```text
codex plugin marketplace add gmaiera/OCI --ref main --sparse .agents/plugins
```

Then install `OCI Codex Skills` from the plugin marketplace and restart Codex so the skills are loaded in new threads.

For repo-local use, the same skills are exposed through:

```text
.agents/skills
```

That directory points back to the maintained source folders under `Codex/skills`.
