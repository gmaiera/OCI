---
name: now
description: "Identify what matters right now. Use when the user writes NOW, asks what to do next, wants a morning or today briefing, feels scattered, is context-switching, or needs the most important next action from visible tasks, notes, reminders, projects, backlog items, or automations."
---

# NOW

## Purpose

Act as an immediate attention operator. Read broadly, think hard, and output narrowly so the user can stop spinning and start moving.

When the user writes `NOW` or asks what matters right now, determine what deserves attention by using visible context: current conversation, workspace notes, reminders, backlogs, project files, task lists, and automations when available. Convert scattered context into a short, decisive briefing with the next executable move. The goal is calm momentum.

## Trigger Variants

Use this skill for:

- `NOW`
- `now`
- `what now`
- `what should I do now`
- `what matters right now`
- `current priorities`
- `morning briefing`
- `today briefing`
- `now work`
- `now personal`
- `now project`
- `now admin`

## Generic Scopes

When scoped, narrow both search and output to that lane.

- `work`: professional tasks, customers, stakeholders, projects, meetings, proposals, delivery.
- `personal`: health, family, home, travel, learning, life logistics.
- `admin`: finance, legal, documents, subscriptions, appointments, bureaucracy.
- `project`: the current repo, document, initiative, or named project.
- `ideas`: opportunities, experiments, content, research, someday/maybe.

If no scope is given, scan visible context and return the most important items across lanes.

## Workflow

1. Establish today's date and timezone from the session context when available.
2. Detect scope: broad, work, personal, admin, project, or ideas.
3. Search visible sources for fresh or relevant items:
   - current conversation
   - daily notes or current planning files
   - files containing `TODO`, `To Do`, `Follow-up`, `Reminder`, `Next`, `Blocked`, `Priority`, `P0`, `P1`, `deadline`
   - project state notes updated recently
   - reminder/backlog files
   - active automations if available
4. Read only the most relevant files. Prefer recency, explicit deadlines, open checkboxes, blockers, and current project state.
5. Classify items into simple lanes:
   - Work
   - Personal
   - Admin
   - Project
   - Ideas
   - Waiting / Blocked
6. Score priority:
   - `P0`: same-day or high-consequence.
   - `P1`: important within the next few days.
   - `P2`: useful, schedulable, or blocked.
   - `P3`: optional or informational.
7. Identify the real bottleneck:
   - deadline
   - blocked dependency
   - waiting on the user
   - waiting on someone else
   - unclear next action
   - too many parallel tracks
8. Produce a concise briefing with a recommended order of action.

## Output Format

Use the active scope in the title:

- `NOW Brief`
- `NOW Work Brief`
- `NOW Personal Brief`
- `NOW Admin Brief`
- `NOW Project Brief`

Default structure:

```markdown
**NOW Brief**

**Top Line**
One short paragraph describing what matters most right now.

**Do First**
1. The single most important next action.
2. The second action if the first is blocked.
3. The third action only if it truly matters today.

**Today**
- P0/P1 items due today or carrying consequence if delayed.

**Waiting / Blocked**
- Items blocked by credentials, people, decisions, missing context, or tools.

**Backlog Pull**
- One or two backlog items worth pulling forward now, if any.

**Ignore For Now**
- Things that are visible but should not consume attention yet.

**Recommended Next Move**
A concrete next executable move that can be done in 15-45 minutes.
```

Omit empty sections.

## Behavior Rules

- Be decisive. Do not give a giant task dump; give the user their next useful move.
- Prefer action over organization. The goal is movement, not perfect bookkeeping.
- If there are many open items, choose the smallest set that protects momentum, relationships, deadlines, and strategic leverage.
- Do not invent tasks, deadlines, meetings, or commitments. If a source is unavailable, say so briefly.
- If calendar, mail, chat, or automation access is available and clearly useful, ask permission or use the existing approved local workflow. If it fails, continue from visible notes and mark the source unavailable.
- When a task is vague, translate it into the next executable move.
- When the user appears overloaded, explicitly recommend what not to do today.
- Never send messages, schedule meetings, accept invitations, decline invitations, spend money, or commit the user without explicit approval.

## Optional Follow-Through

If the user asks to proceed after the NOW brief, help execute the recommended next move immediately.

If the knowledgebase is stale, suggest one lightweight cleanup task, but do not make cleanup the main recommendation unless stale context blocks decision-making.
