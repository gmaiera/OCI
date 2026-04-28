---
name: pipeline
description: "Organize messy work into a clear execution pipeline. Use when the user wants to sort ideas, requests, opportunities, projects, tasks, deals, content, research, or initiatives into stages with priorities, owners, next actions, blockers, and follow-up cadence."
---

# Pipeline

## Purpose

Turn scattered work into a visible operating pipeline that helps people decide what to do next, what to defer, what is blocked, and what should be shipped.

Use this skill for daily work organization, project intake, sales or opportunity tracking, idea backlogs, content calendars, research queues, hiring steps, partner motions, or any situation where multiple items need flow instead of a flat task list.

## Default Pipeline

Use these stages unless the user already has a better workflow:

```text
Inbox -> Clarify -> Prioritize -> Doing -> Waiting -> Done -> Archive
```

For each item, capture:

- Name.
- Outcome desired.
- Current stage.
- Priority: P0, P1, P2, or Someday.
- Owner.
- Next action.
- Blocker or dependency.
- Due date or review date.
- Evidence, link, or source if available.

## Workflow

1. Identify the pipeline domain: personal tasks, work projects, sales, research, hiring, content, ideas, or mixed.
2. Collect or infer items from the user's notes, files, pasted text, or conversation.
3. Normalize each item into one row with a clear next action.
4. Remove duplicates and merge related items.
5. Flag stale, blocked, risky, or high-leverage items.
6. Recommend the smallest useful operating cadence: daily, weekly, biweekly, or milestone-based.
7. Produce a pipeline table and a short action plan.

If the user only wants execution, skip heavy categorization and produce the next 3-5 moves.

## Priority Rules

Use priority labels consistently:

- `P0`: urgent or high-consequence; act today.
- `P1`: important; act this week.
- `P2`: useful; schedule or batch.
- `Someday`: keep visible but do not spend active attention now.

Prioritize based on:

- Deadline or aging.
- Strategic value.
- Relationship or customer impact.
- Revenue, cost, or risk.
- Blocking effect on other work.
- Effort versus payoff.

Do not treat loudness as importance. If everything looks urgent, create a forced ranking.

## Output Format

Prefer this format:

```markdown
**Pipeline**
| Stage | Priority | Item | Owner | Next Action | Blocker | Review |
|---|---|---|---|---|---|---|

**Top Moves**
1. [Action] - [why now]
2. [Action] - [why now]
3. [Action] - [why now]

**Blocked / Waiting**
- [Item]: waiting on [person/system/input]. Follow up [date/cadence].

**Maintenance**
- Review cadence:
- Items to archive:
- Items that need clarification:
```

When the user asks for a durable artifact, create or update a Markdown, CSV, spreadsheet, GitHub issue list, or project board format that fits their environment.

## Quality Bar

Before finalizing, check:

- Every active item has one next action.
- Priority is forced, not vague.
- Blocked items name the dependency.
- The output is usable today.
- The pipeline has a review cadence.
- The user can copy the table into their preferred tool.

## Failure Modes To Avoid

- Do not create a beautiful taxonomy with no next actions.
- Do not bury the most important item in a long table.
- Do not expand the process beyond what the work deserves.
- Do not assume a specific app unless the user names one.
- Do not invent owners or due dates; label them `TBD` when unknown.

