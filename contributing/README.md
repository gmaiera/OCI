# Contributing

Contributions should make OCI easier to use without weakening the public safety boundary.

## Good Contributions

- Add or improve a reusable skill.
- Make navigation clearer for first-time visitors.
- Add public-safe guides, examples, tests, or validation notes.
- Improve redaction, provenance, or privacy review patterns.

## Public Safety

Do not include credentials, private transcripts, internal strategy, private client or partner details, local runtime state, or unapproved drafts.

Review these before opening a pull request:

- [Publication checklist](../PUBLICATION_CHECKLIST.md)
- [Security policy](../SECURITY.md)
- [Codex skill system check](../Codex/SYSTEM_CHECK.md)

## Skill Release Path

Public Codex skills move through:

```text
Codex/skills-lab/sandbox
  -> Codex/skills-lab/candidates
  -> Codex/skills-lab/production
  -> Codex/skills
```

The visitor-friendly `skills/` folder should describe what is available; the plugin-compatible implementation stays in `Codex/skills`.
