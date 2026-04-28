# Codex

Welcome to the Codex skills lab.

This folder is where we build, test, polish, and share small AI work rituals that help people have better days: clearer focus, smoother collaboration, sharper research, stronger artifacts, and less friction between "we should do this" and "it is shipped."

The intended GitHub location is:

```text
https://github.com/gmaiera/OCI/tree/main/Codex
```

## Operating Model

Skills move through a simple path from experiment to shared tool:

```text
skills-lab/sandbox
  -> skills-lab/candidates
  -> skills-lab/production
  -> skills
```

- `skills-lab/sandbox`: private experiments that can be installed locally for hands-on testing.
- `skills-lab/candidates`: skills that passed basic local testing and are ready for final review.
- `skills-lab/production`: skills that are approved for local Codex use.
- `skills`: public/shareable skill packages prepared for GitHub.

The local runtime install location is:

```text
~/.codex/skills
```

That folder is what Codex actually loads. The lab is where skills are designed, validated, promoted, and prepared for sharing.

## Public Sharing Philosophy

The public `skills/` folder is for skills that help people work better every day, with a little more flow and a lot less fog:

- Make better decisions.
- Do better research.
- Ship focused work.
- Communicate ideas clearly.
- Create useful deliverables with less friction.

Personal operating-system skills should stay private unless they are rewritten generically and pass a privacy review.

Personal operating-system skills should stay private unless they are rewritten generically and pass a privacy review. The vibe is generous, but the privacy bar stays high.

See `SYSTEM_CHECK.md` for the current inventory and shareability assessment.

See `WORKFLOW.md` for how these skills combine into an organization-wide performance improvement workflow.

## Normal Workflow

Use this loop when creating or improving a skill:

1. Create or edit a skill in `skills-lab/sandbox/<skill-name>`.
2. Validate the skill:

   ```text
   python3 skills-lab/scripts/validate_skill.py skills-lab/sandbox/<skill-name>
   ```

3. Install it locally for testing:

   ```text
   python3 skills-lab/scripts/install_local.py skills-lab/sandbox/<skill-name>
   ```

4. Run the skill from Codex and capture eval notes in `skills-lab/evals/<skill-name>/prompts.md`.
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

Do not edit `~/.codex/skills/<skill-name>` directly. Keep the groove clean: make changes in `skills-lab/sandbox`, test them locally, then promote again.

## GitHub Sharing Rule

Only files under `Codex/skills` are intended to be shared publicly. Treat everything under `skills-lab` as local working material unless you explicitly decide otherwise.
