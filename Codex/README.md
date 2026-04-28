# Codex

This folder is the local working area for building, testing, promoting, and sharing Codex skills.

The intended GitHub location is:

```text
https://github.com/gmaiera/OCI/tree/main/Codex
```

## Operating Model

Skills move through four stages:

```text
skills-lab/sandbox
  -> skills-lab/candidates
  -> skills-lab/production
  -> skills
```

- `skills-lab/sandbox`: private experiments that can be installed locally for hands-on testing.
- `skills-lab/candidates`: skills that passed basic local testing and are ready for final review.
- `skills-lab/production`: skills that are approved for Gustavo's local Codex environment.
- `skills`: public/shareable skill packages prepared for GitHub.

The local runtime install location is:

```text
~/.codex/skills
```

That folder is what Codex actually loads. The lab is where skills are designed, validated, promoted, and prepared for sharing.

## Public Sharing Philosophy

The public `skills/` folder is for skills that help people work better every day:

- Make better decisions.
- Do better research.
- Ship focused work.
- Communicate ideas clearly.
- Create useful deliverables with less friction.

Personal operating-system skills should stay private unless they are rewritten generically and pass a privacy review.

See `SYSTEM_CHECK.md` for the current inventory, shareability assessment, and recommended next skills to publish.

## Normal Workflow

1. Create or edit a skill in `skills-lab/sandbox/<skill-name>`.
2. Validate the skill:

   ```text
   python3 skills-lab/scripts/validate_skill.py skills-lab/sandbox/<skill-name>
   ```

3. Install it locally for testing:

   ```text
   python3 skills-lab/scripts/install_local.py skills-lab/sandbox/<skill-name>
   ```

4. Run the skill from Codex on this computer and capture eval notes in `skills-lab/evals/<skill-name>/prompts.md`.
5. Nominate the reviewed skill as a candidate:

   ```text
   python3 skills-lab/scripts/nominate_candidate.py <skill-name>
   ```

6. Promote it into local production:

   ```text
   python3 skills-lab/scripts/promote_local.py <skill-name>
   ```

7. Prepare a GitHub-safe copy:

   ```text
   python3 skills-lab/scripts/prepare_github_release.py <skill-name>
   ```

8. Review the generated package in `skills/<skill-name>` before committing and pushing the repo.

## Production Rule

Do not edit `~/.codex/skills/<skill-name>` directly. Make changes in `skills-lab/sandbox`, test them locally, then promote again.

## GitHub Sharing Rule

Only files under `Codex/skills` are intended to be shared publicly. Treat everything under `skills-lab` as local working material unless you explicitly decide otherwise.
