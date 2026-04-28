# Skill Eval: now

## Trigger Prompt

```text
NOW. I feel scattered. What should I do first?
```

Expected result:

```text
The answer produces a concise NOW Brief with a top line, do-first actions, waiting/blocked items if visible, and a concrete next move.
```

## Negative Prompt

```text
Create a long project backlog.
```

Expected behavior:

```text
Prefer pipeline over NOW unless the user asks what to do right now.
```

