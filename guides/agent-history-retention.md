# Agent History Retention And Insights

This guide helps people keep useful local AI-agent history long enough to learn from it, back it up privately, and extract review-only lessons without publishing raw transcripts.

If you want the community package implemented in another repository, use the **Copy This Once And Run** block below.

The original implementation plan follows so another agent or engineer can build the package without making new product decisions.

---

## Implementation Plan

> **Watermark / provenance:** OCI Community Contribution built by github.com/gmaiera - Review before use

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a public, privacy-first, one-time best-practice kit that helps people retain local AI-agent history, back it up safely, and extract reviewable lessons across Claude Code, OpenAI Codex, and other coding agents.

**Architecture:** Ship a vendor-neutral `agent-history-retention` package with provider adapters, example configuration files, run-once backup and insight scripts, JSON schemas, tests, documentation, and provenance watermarking. Provider-specific settings stay in examples, while the scripts use an adapter interface so future agents can be added without rewriting the core flow.

**Tech Stack:** Markdown, Node.js ESM, JSONL, JSON Schema, TOML examples, GitHub Actions, shell-safe CLI commands.

---

## What This Is

This is a one-time local setup pattern for people who treat AI-agent sessions as valuable work history. It helps Claude Code, OpenAI Codex, and other agent users keep useful local history for 365 days, create a private backup, and extract human-reviewed lessons from that history.

It is not a daemon, cron job, recurring automation, background service, or transcript publishing pipeline. Run it once, review the output, keep what helps, and forget the tool until you intentionally run it again.

## Why Implement

Are your sessions very important? Do you keep them for how long? Do you allow your agents to learn from them? Read this.

Agent sessions often contain the best record of how work actually happened: what failed, what recovered, what preferences repeated, and what the next agent should stop doing. If those sessions disappear too quickly, every future agent starts colder than it needs to. This policy keeps history long enough to learn from it while keeping raw transcripts private by default.

## Copy This Once And Run

Copy this single text block into Claude Code, Codex, or another coding agent when you want it to implement the community package from this plan:

```text
Implement the one-time Agent History Retention And Insights community package in this repository.

Purpose:
- Preserve local AI-agent session history for 365 days when the provider supports it.
- Back up useful local history and memory files without copying auth, logs, caches, attachments, shell snapshots, local databases, or temporary files.
- Generate review-only insights so agents can learn from repeated blockers, user preferences, successful recovery patterns, project frequency, and "do differently next time" rules.
- Keep raw transcripts private and never auto-write generated lessons into AGENTS.md, Claude instructions, Codex memories, or repo docs.

Watermark:
Use this exact watermark in public docs and generated artifact provenance:
"OCI Community Contribution built by github.com/gmaiera - Review before use"

Source:
This policy is an improvement from the public source idea at https://x.com/ArtemXTech/status/2061146280802316741?s=20 and must stay open to improvements from the open source community through pull requests.

Provider rules:
- For Claude Code, include a documented settings example with "cleanupPeriodDays": 365.
- For OpenAI Codex, do not add cleanupPeriodDays. Use supported Codex settings only:
  [history].persistence = "save-all"
  [features].memories = true
  [memories].generate_memories = true
  [memories].use_memories = true
- For other agents, use an adapter contract instead of pretending every provider has the same retention setting.

Execution:
- Build the files, tests, docs, examples, and validation workflow described in this plan.
- Use only synthetic fixtures.
- Exclude private local paths, secrets, customer data, internal URLs, and raw transcripts.
- Run tests and public-safety scans before opening a PR.
```

Implementation steps come first. Detailed privacy and source explanations are collected at the end of this document.

## Provenance Policy

All generated artifacts from this project must include a provenance block with:

```yaml
artifact_id: "agent-history-retention-<artifact-kind>-<date>"
classification: "public-template"
review_status: "draft"
created_with: "AI-assisted workflow"
source_docs:
  - "https://x.com/ArtemXTech/status/2061146280802316741?s=20"
  - "https://code.claude.com/docs/en/settings"
  - "https://developers.openai.com/codex/config-reference"
  - "https://developers.openai.com/codex/config-advanced#config-and-state-locations"
  - "https://developers.openai.com/codex/memories"
  - "https://developers.openai.com/codex/cli/reference#codex-archive-and-codex-unarchive"
watermark: "<standard watermark shown at the top of this plan>"
```

The watermark is provenance and review status, not a decorative overlay. Use the full text only in the most visible attribution points and in machine-readable artifact provenance. Raw transcripts, secrets, local usernames, private paths, customer data, and organization-internal context must never be committed.

## Community Source And PRs

This policy is an improvement from the public source idea at <https://x.com/ArtemXTech/status/2061146280802316741?s=20>. Treat that post as inspiration for the problem statement, then ground implementation details in provider documentation and local privacy review.

Open source improvements are welcome as pull requests. Good PRs should add provider adapters, safer redaction, better synthetic fixtures, clearer docs, or new tests without weakening the privacy contract.

## Proposed File Structure

- Create: `Codex/agent-history-retention/README.md`
  - Public overview, supported agents, safety model, quickstart, and restore notes.
- Create: `Codex/agent-history-retention/docs/source-findings.md`
  - Source-backed explanation of Claude, Codex, and provider-neutral behavior.
- Create: `Codex/agent-history-retention/docs/review-and-apply-lessons.md`
  - Human review process for promoting candidate lessons into `AGENTS.md`, Claude instructions, repo docs, or private memory.
- Create: `Codex/agent-history-retention/config/claude-settings.example.json`
  - Claude Code example with `cleanupPeriodDays: 365`.
- Create: `Codex/agent-history-retention/config/codex-config.example.toml`
  - Codex example with supported history and memory settings only.
- Create: `Codex/agent-history-retention/config/agent-history.policy.example.json`
  - Vendor-neutral policy describing retention days, allowed sources, exclusions, and output paths.
- Create: `Codex/agent-history-retention/scripts/agent-history-backup.mjs`
  - CLI for safe local backups using provider adapters.
- Create: `Codex/agent-history-retention/scripts/agent-history-insights.mjs`
  - CLI for local lesson extraction from session JSONL and memory-like files.
- Create: `Codex/agent-history-retention/scripts/lib/adapters.mjs`
  - Agent adapter registry for Claude, Codex, and custom providers.
- Create: `Codex/agent-history-retention/scripts/lib/redaction.mjs`
  - Deterministic redaction and prompt-text gating helpers.
- Create: `Codex/agent-history-retention/scripts/lib/provenance.mjs`
  - Provenance and sidecar manifest helpers.
- Create: `Codex/agent-history-retention/schemas/backup-manifest.schema.json`
  - Machine-readable backup manifest schema.
- Create: `Codex/agent-history-retention/schemas/insights.schema.json`
  - Machine-readable insight report schema.
- Create: `Codex/agent-history-retention/templates/candidate-agent-lessons.md`
  - Review-only lesson template.
- Create: `Codex/agent-history-retention/templates/AGENTS.history-lessons.example.md`
  - Example of sanitized lessons after human approval.
- Create: `Codex/agent-history-retention/tests/backup.test.mjs`
  - Fixture tests for source inclusion, exclusions, retention, dry-run behavior, and archive manifest shape.
- Create: `Codex/agent-history-retention/tests/insights.test.mjs`
  - Fixture tests for JSONL parsing, privacy gating, lesson extraction, and watermark metadata.
- Create: `Codex/agent-history-retention/tests/fixtures/`
  - Tiny synthetic Claude, Codex, and generic agent session samples.
- Create: `.github/workflows/agent-history-retention.yml`
  - CI for Node tests and public-content scanning.
- Modify: `Codex/README.md`
  - Add a link to the new community package.
- Modify: `README.md`
  - Add a short pointer from the repo root to the community package.

## Task 1: Add Public Package Shell And Source Findings

**Files:**
- Create: `Codex/agent-history-retention/README.md`
- Create: `Codex/agent-history-retention/docs/source-findings.md`
- Modify: `Codex/README.md`
- Modify: `README.md`

- [ ] **Step 1: Create the package README**

Write `Codex/agent-history-retention/README.md`:

```markdown
# Agent History Retention And Insights

> **Watermark / provenance:** OCI Community Contribution built by github.com/gmaiera - Review before use

Are your sessions very important? Do you keep them for how long? Do you allow your agents to learn from them? Read this.

This package shows how to preserve local coding-agent history for personal learning without publishing raw transcripts. It is a one-time setup and review workflow, not a daemon, cron job, recurring automation, or background service.

It supports three lanes:

1. Claude Code settings examples.
2. OpenAI Codex settings examples.
3. A vendor-neutral backup and insights interface for other local agents.

## Origin

This policy is an improvement from the public source idea at <https://x.com/ArtemXTech/status/2061146280802316741?s=20>. Implementation details are grounded in Claude Code and OpenAI Codex documentation plus community review.

## What This Solves

- Keep local agent history available long enough to learn from it.
- Back up useful session and memory files without copying auth, cache, logs, or attachments.
- Extract candidate lessons such as repeated blockers, preferences, successful recovery patterns, project frequency, and "do differently next time" rules.
- Keep those lessons human-reviewed before they become durable agent instructions.

## Copy This Once And Run

```text
Run the local agent-history retention check once for my agent home. Keep raw transcripts private, exclude auth/log/cache/attachment/database/temp files, generate review-only candidate lessons, and use the standard OCI Community Contribution provenance watermark in generated outputs.
```

## What This Does Not Do

- It does not publish raw transcripts.
- It does not sync private sessions to a public repository.
- It does not invent unsupported agent configuration keys.
- It does not automatically edit `AGENTS.md`, Claude instructions, or memory files.
- It does not schedule itself or run continuously.

## Run Once

```bash
node scripts/agent-history-backup.mjs --agent codex --retention-days 365 --dry-run
node scripts/agent-history-insights.mjs --agent codex --since-days 365 --output-dir ./out/codex-history-insights
```

For Claude Code, use the example settings in `config/claude-settings.example.json`.

For Codex, use the supported example settings in `config/codex-config.example.toml`.

Review `out/codex-history-insights/candidate-agent-lessons.md` before copying any lesson into checked-in agent guidance.

## Safety Defaults

- Prompt text is excluded unless `--include-prompts` is explicitly set.
- Backups exclude auth, logs, caches, attachments, shell snapshots, local databases, and temporary directories.
- Every generated report includes a provenance watermark.
- Public fixture files are synthetic.

## Community Improvements

Pull requests are welcome for safer adapters, better redaction, stronger tests, clearer docs, and additional provider examples.
```

- [ ] **Step 2: Add source findings**

Write `Codex/agent-history-retention/docs/source-findings.md`:

```markdown
# Source Findings

## Origin

This policy is an improvement from the public source idea at <https://x.com/ArtemXTech/status/2061146280802316741?s=20>. The implementation improves the idea by making it provider-specific, private by default, one-time by design, and open to pull-request improvements from the community.

## Claude Code

Claude Code documents `cleanupPeriodDays` in settings as the cleanup period for old chat transcripts. A 365-day local-history policy can be represented in Claude settings with:

```json
{
  "cleanupPeriodDays": 365
}
```

Source: <https://code.claude.com/docs/en/settings>

## OpenAI Codex

Codex does not document `cleanupPeriodDays` as a supported config key.

Use supported Codex controls instead:

```toml
[history]
persistence = "save-all"

[features]
memories = true

[memories]
generate_memories = true
use_memories = true
```

Codex stores local state under `CODEX_HOME`, which defaults to `~/.codex`. Relevant state includes `config.toml`, `history.jsonl`, `sessions/`, `archived_sessions/`, and `memories/`.

Useful source pages:

- <https://developers.openai.com/codex/config-reference>
- <https://developers.openai.com/codex/config-advanced#config-and-state-locations>
- <https://developers.openai.com/codex/memories>
- <https://developers.openai.com/codex/cli/reference#codex-archive-and-codex-unarchive>
- <https://developers.openai.com/codex/guides/agents-md>
- <https://developers.openai.com/codex/skills>

## Other Agents

Other local agents should integrate through a small adapter contract:

- `name`
- `defaultHome`
- `configFiles`
- `historySources`
- `memorySources`
- `exclusions`
- `detectSessionTime(record)`
- `extractProject(record)`
- `extractLessons(record)`

Do not assume every agent has the same retention setting. Prefer a local backup policy plus documented provider-specific settings.
```

- [ ] **Step 3: Link from `Codex/README.md`**

Add this section after the existing operating model:

```markdown
## Community Best Practices

- `agent-history-retention/`: public-safe plan and toolkit for keeping local agent history useful across Claude Code, OpenAI Codex, and other coding agents without publishing raw transcripts.
```

- [ ] **Step 4: Link from root `README.md`**

Add this bullet under the project description:

```markdown
- `Codex/agent-history-retention/`: community best practices for private agent-history backups, retention, insight extraction, and provenance watermarking.
```

- [ ] **Step 5: Verify no private local paths**

Run:

```bash
rg -n "/U[s]ers/|Oracle confidential|customer data|private key|t[o]ken=" Codex/agent-history-retention README.md Codex/README.md
```

Expected: no matches.

- [ ] **Step 6: Commit**

```bash
git add README.md Codex/README.md Codex/agent-history-retention/README.md Codex/agent-history-retention/docs/source-findings.md
git commit -m "docs: add agent history retention source findings"
```

## Task 2: Add Provider Configuration Examples

**Files:**
- Create: `Codex/agent-history-retention/config/claude-settings.example.json`
- Create: `Codex/agent-history-retention/config/codex-config.example.toml`
- Create: `Codex/agent-history-retention/config/agent-history.policy.example.json`

- [ ] **Step 1: Add Claude settings example**

Write `Codex/agent-history-retention/config/claude-settings.example.json`:

```json
{
  "cleanupPeriodDays": 365
}
```

- [ ] **Step 2: Add Codex config example**

Write `Codex/agent-history-retention/config/codex-config.example.toml`:

```toml
[history]
persistence = "save-all"

[features]
memories = true

[memories]
generate_memories = true
use_memories = true
```

- [ ] **Step 3: Add neutral policy example**

Write `Codex/agent-history-retention/config/agent-history.policy.example.json`:

```json
{
  "$schema": "../schemas/agent-history-policy.schema.json",
  "watermark": "standard-provenance-watermark",
  "retentionDays": 365,
  "promptTextDefault": false,
  "backup": {
    "archive": false,
    "includeSources": [
      "sessions",
      "archived_sessions",
      "history",
      "session_index",
      "memories"
    ],
    "excludeGlobs": [
      "**/auth.json",
      "**/*token*",
      "**/*.sqlite",
      "**/*.sqlite-shm",
      "**/*.sqlite-wal",
      "**/logs/**",
      "**/log/**",
      "**/attachments/**",
      "**/plugins/**",
      "**/cache/**",
      "**/shell_snapshots/**",
      "**/tmp/**",
      "**/.tmp/**"
    ]
  },
  "insights": {
    "topProjectsLimit": 20,
    "lessonLimit": 100,
    "includePrompts": false
  }
}
```

- [ ] **Step 4: Verify examples parse**

Run:

```bash
node -e "JSON.parse(require('fs').readFileSync('Codex/agent-history-retention/config/claude-settings.example.json','utf8')); JSON.parse(require('fs').readFileSync('Codex/agent-history-retention/config/agent-history.policy.example.json','utf8')); console.log('json ok')"
```

Expected:

```text
json ok
```

- [ ] **Step 5: Commit**

```bash
git add Codex/agent-history-retention/config
git commit -m "docs: add cross-agent history configuration examples"
```

## Task 3: Add Schemas And Provenance Helpers

**Files:**
- Create: `Codex/agent-history-retention/schemas/agent-history-policy.schema.json`
- Create: `Codex/agent-history-retention/schemas/backup-manifest.schema.json`
- Create: `Codex/agent-history-retention/schemas/insights.schema.json`
- Create: `Codex/agent-history-retention/scripts/lib/provenance.mjs`

- [ ] **Step 1: Add policy schema**

Write `Codex/agent-history-retention/schemas/agent-history-policy.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/gmaiera/OCI/Codex/agent-history-retention/schemas/agent-history-policy.schema.json",
  "title": "Agent History Policy",
  "type": "object",
  "required": ["watermark", "retentionDays", "promptTextDefault", "backup", "insights"],
  "properties": {
    "watermark": { "type": "string", "minLength": 1 },
    "retentionDays": { "type": "integer", "minimum": 1 },
    "promptTextDefault": { "type": "boolean" },
    "backup": {
      "type": "object",
      "required": ["archive", "includeSources", "excludeGlobs"],
      "properties": {
        "archive": { "type": "boolean" },
        "includeSources": { "type": "array", "items": { "type": "string" } },
        "excludeGlobs": { "type": "array", "items": { "type": "string" } }
      },
      "additionalProperties": false
    },
    "insights": {
      "type": "object",
      "required": ["topProjectsLimit", "lessonLimit", "includePrompts"],
      "properties": {
        "topProjectsLimit": { "type": "integer", "minimum": 1 },
        "lessonLimit": { "type": "integer", "minimum": 1 },
        "includePrompts": { "type": "boolean" }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

- [ ] **Step 2: Add backup manifest schema**

Write `Codex/agent-history-retention/schemas/backup-manifest.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/gmaiera/OCI/Codex/agent-history-retention/schemas/backup-manifest.schema.json",
  "title": "Agent History Backup Manifest",
  "type": "object",
  "required": ["artifact_id", "watermark", "agent", "createdAt", "retentionDays", "dryRun", "files", "excludedPatterns"],
  "properties": {
    "artifact_id": { "type": "string" },
    "watermark": { "type": "string" },
    "agent": { "type": "string" },
    "createdAt": { "type": "string", "format": "date-time" },
    "retentionDays": { "type": "integer", "minimum": 1 },
    "dryRun": { "type": "boolean" },
    "archivePath": { "type": ["string", "null"] },
    "files": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["source", "relativePath", "bytes", "mtime"],
        "properties": {
          "source": { "type": "string" },
          "relativePath": { "type": "string" },
          "bytes": { "type": "integer", "minimum": 0 },
          "mtime": { "type": "string", "format": "date-time" }
        },
        "additionalProperties": false
      }
    },
    "excludedPatterns": { "type": "array", "items": { "type": "string" } }
  },
  "additionalProperties": false
}
```

- [ ] **Step 3: Add insights schema**

Write `Codex/agent-history-retention/schemas/insights.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/gmaiera/OCI/Codex/agent-history-retention/schemas/insights.schema.json",
  "title": "Agent History Insights",
  "type": "object",
  "required": ["artifact_id", "watermark", "agent", "generatedAt", "sinceDays", "promptTextIncluded", "summary", "topProjects", "lessons"],
  "properties": {
    "artifact_id": { "type": "string" },
    "watermark": { "type": "string" },
    "agent": { "type": "string" },
    "generatedAt": { "type": "string", "format": "date-time" },
    "sinceDays": { "type": "integer", "minimum": 1 },
    "promptTextIncluded": { "type": "boolean" },
    "summary": {
      "type": "object",
      "required": ["sessions", "activeDays", "turns", "parseErrors"],
      "properties": {
        "sessions": { "type": "integer", "minimum": 0 },
        "activeDays": { "type": "integer", "minimum": 0 },
        "turns": { "type": "integer", "minimum": 0 },
        "parseErrors": { "type": "integer", "minimum": 0 }
      },
      "additionalProperties": false
    },
    "topProjects": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["project", "count"],
        "properties": {
          "project": { "type": "string" },
          "count": { "type": "integer", "minimum": 1 }
        },
        "additionalProperties": false
      }
    },
    "lessons": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["kind", "text", "source"],
        "properties": {
          "kind": { "enum": ["preference", "blocker", "recovery", "do_differently"] },
          "text": { "type": "string" },
          "source": { "type": "string" }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```

- [ ] **Step 4: Add provenance helper**

Write `Codex/agent-history-retention/scripts/lib/provenance.mjs`:

```js
export function buildArtifactId(kind, date = new Date()) {
  const stamp = date.toISOString().slice(0, 10);
  return `agent-history-retention-${kind}-${stamp}`;
}

export function buildWatermark(kind, date = new Date()) {
  return "OCI Community Contribution built by github.com/gmaiera - Review before use";
}

export function withProvenance(kind, payload, date = new Date()) {
  return {
    artifact_id: buildArtifactId(kind, date),
    watermark: buildWatermark(kind, date),
    ...payload
  };
}
```

- [ ] **Step 5: Commit**

```bash
git add Codex/agent-history-retention/schemas Codex/agent-history-retention/scripts/lib/provenance.mjs
git commit -m "feat: add agent history provenance schemas"
```

## Task 4: Add Adapter And Redaction Core

**Files:**
- Create: `Codex/agent-history-retention/scripts/lib/adapters.mjs`
- Create: `Codex/agent-history-retention/scripts/lib/redaction.mjs`

- [ ] **Step 1: Add adapter registry**

Write `Codex/agent-history-retention/scripts/lib/adapters.mjs`:

```js
import os from "node:os";
import path from "node:path";

const home = os.homedir();

export const adapters = {
  codex: {
    name: "codex",
    defaultHome: process.env.CODEX_HOME || path.join(home, ".codex"),
    configFiles: ["config.toml"],
    historySources: ["sessions", "archived_sessions", "session_index.jsonl", "history.jsonl"],
    memorySources: ["memories"],
    exclusions: [
      "auth.json",
      "*.sqlite",
      "*.sqlite-shm",
      "*.sqlite-wal",
      "log/**",
      "logs/**",
      "attachments/**",
      "plugins/**",
      "cache/**",
      "shell_snapshots/**",
      "tmp/**",
      ".tmp/**"
    ]
  },
  claude: {
    name: "claude",
    defaultHome: process.env.CLAUDE_CONFIG_DIR || path.join(home, ".claude"),
    configFiles: ["settings.json"],
    historySources: ["projects"],
    memorySources: [],
    exclusions: [
      "*token*",
      "*auth*",
      "logs/**",
      "cache/**",
      "tmp/**",
      ".tmp/**"
    ]
  },
  generic: {
    name: "generic",
    defaultHome: process.cwd(),
    configFiles: [],
    historySources: ["sessions", "history.jsonl"],
    memorySources: ["memories"],
    exclusions: [
      "*token*",
      "*auth*",
      "*.sqlite",
      "*.sqlite-shm",
      "*.sqlite-wal",
      "logs/**",
      "cache/**",
      "attachments/**",
      "tmp/**",
      ".tmp/**"
    ]
  }
};

export function getAdapter(name) {
  const adapter = adapters[name];
  if (!adapter) {
    throw new Error(`Unknown agent adapter: ${name}`);
  }
  return adapter;
}
```

- [ ] **Step 2: Add redaction helper**

Write `Codex/agent-history-retention/scripts/lib/redaction.mjs`:

```js
const patterns = [
  [/sk-[A-Za-z0-9_-]{12,}/g, "[REDACTED_OPENAI_KEY]"],
  [/(api[_-]?key|token|secret|password)\s*[:=]\s*["']?[^"'\s]+/gi, "$1=[REDACTED]"],
  [/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi, "[REDACTED_EMAIL]"],
  [/-----B[E]GIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----E[N]D [A-Z ]*PRIVATE KEY-----/g, "[REDACTED_PRIVATE_KEY]"]
];

export function redactText(value) {
  let text = String(value ?? "");
  for (const [pattern, replacement] of patterns) {
    text = text.replace(pattern, replacement);
  }
  return text;
}

export function safePromptSample(value, includePrompts) {
  if (!includePrompts) {
    return "";
  }
  return redactText(value).slice(0, 500);
}
```

- [ ] **Step 3: Verify modules import**

Run:

```bash
node -e "import('./Codex/agent-history-retention/scripts/lib/adapters.mjs').then(m => console.log(Object.keys(m.adapters).join(',')))"
```

Expected:

```text
codex,claude,generic
```

- [ ] **Step 4: Commit**

```bash
git add Codex/agent-history-retention/scripts/lib/adapters.mjs Codex/agent-history-retention/scripts/lib/redaction.mjs
git commit -m "feat: add agent adapter and redaction core"
```

## Task 5: Add Backup CLI With Tests

**Files:**
- Create: `Codex/agent-history-retention/scripts/agent-history-backup.mjs`
- Create: `Codex/agent-history-retention/tests/backup.test.mjs`
- Create: `Codex/agent-history-retention/tests/fixtures/codex-home/`
- Create: `Codex/agent-history-retention/tests/fixtures/claude-home/`

- [ ] **Step 1: Create synthetic fixtures**

Create these files:

```text
Codex/agent-history-retention/tests/fixtures/codex-home/sessions/session-1.jsonl
Codex/agent-history-retention/tests/fixtures/codex-home/archived_sessions/session-2.jsonl
Codex/agent-history-retention/tests/fixtures/codex-home/history.jsonl
Codex/agent-history-retention/tests/fixtures/codex-home/session_index.jsonl
Codex/agent-history-retention/tests/fixtures/codex-home/memories/MEMORY.md
Codex/agent-history-retention/tests/fixtures/codex-home/auth.json
Codex/agent-history-retention/tests/fixtures/codex-home/logs/debug.log
Codex/agent-history-retention/tests/fixtures/claude-home/settings.json
Codex/agent-history-retention/tests/fixtures/claude-home/projects/demo/session.jsonl
Codex/agent-history-retention/tests/fixtures/claude-home/cache/cache.bin
```

Use synthetic text such as:

```json
{"timestamp":"2026-06-01T12:00:00.000Z","cwd":"/workspace/demo","type":"turn","message":"synthetic public fixture"}
```

- [ ] **Step 2: Write failing backup test**

Write `Codex/agent-history-retention/tests/backup.test.mjs`:

```js
import assert from "node:assert/strict";
import { mkdtemp, readFile, stat } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";

const root = path.resolve("Codex/agent-history-retention");
const script = path.join(root, "scripts/agent-history-backup.mjs");
const fixture = path.join(root, "tests/fixtures/codex-home");

test("dry run includes approved files and excludes auth, logs, and caches", async () => {
  const result = spawnSync(process.execPath, [
    script,
    "--agent", "codex",
    "--home", fixture,
    "--retention-days", "365",
    "--dry-run",
    "--now", "2026-06-27T00:00:00.000Z"
  ], { encoding: "utf8" });

  assert.equal(result.status, 0, result.stderr);
  const manifest = JSON.parse(result.stdout);
  assert.equal(manifest.dryRun, true);
  assert.equal(manifest.retentionDays, 365);
  assert.ok(manifest.files.some(file => file.relativePath === "sessions/session-1.jsonl"));
  assert.ok(manifest.files.some(file => file.relativePath === "memories/MEMORY.md"));
  assert.ok(!manifest.files.some(file => file.relativePath.includes("auth.json")));
  assert.ok(!manifest.files.some(file => file.relativePath.includes("debug.log")));
  assert.match(manifest.watermark, /OCI Community Contribution/);
});

test("apply writes manifest to output directory", async () => {
  const output = await mkdtemp(path.join(tmpdir(), "agent-history-backup-"));
  const result = spawnSync(process.execPath, [
    script,
    "--agent", "codex",
    "--home", fixture,
    "--output-dir", output,
    "--retention-days", "365",
    "--apply",
    "--timestamp", "20260627T000000Z",
    "--now", "2026-06-27T00:00:00.000Z"
  ], { encoding: "utf8" });

  assert.equal(result.status, 0, result.stderr);
  const summary = JSON.parse(result.stdout);
  const manifestPath = path.join(summary.backupDir, "manifest.json");
  const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
  assert.equal(manifest.files.length > 0, true);
  await stat(path.join(summary.backupDir, "sessions/session-1.jsonl"));
});
```

- [ ] **Step 3: Implement minimal backup CLI**

Write `Codex/agent-history-retention/scripts/agent-history-backup.mjs` with this behavior:

```js
#!/usr/bin/env node
import { cp, mkdir, readdir, stat, writeFile } from "node:fs/promises";
import path from "node:path";
import { getAdapter } from "./lib/adapters.mjs";
import { withProvenance } from "./lib/provenance.mjs";

function parseArgs(argv) {
  const args = { agent: "codex", retentionDays: 365, dryRun: true, apply: false, archive: false };
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--agent") args.agent = argv[++index];
    else if (arg === "--home") args.home = argv[++index];
    else if (arg === "--output-dir") args.outputDir = argv[++index];
    else if (arg === "--retention-days") args.retentionDays = Number(argv[++index]);
    else if (arg === "--apply") { args.apply = true; args.dryRun = false; }
    else if (arg === "--dry-run") { args.dryRun = true; args.apply = false; }
    else if (arg === "--archive") args.archive = true;
    else if (arg === "--now") args.now = argv[++index];
    else if (arg === "--timestamp") args.timestamp = argv[++index];
    else throw new Error(`Unknown argument: ${arg}`);
  }
  return args;
}

function isExcluded(relativePath, adapter) {
  return adapter.exclusions.some(pattern => {
    const normalized = relativePath.replaceAll(path.sep, "/");
    if (pattern.endsWith("/**")) return normalized.startsWith(pattern.slice(0, -3));
    if (pattern.startsWith("*")) return normalized.endsWith(pattern.slice(1));
    return normalized === pattern || normalized.includes(`/${pattern}`);
  });
}

async function walk(base, root, adapter, cutoff, files) {
  const entries = await readdir(base, { withFileTypes: true }).catch(() => []);
  for (const entry of entries) {
    const absolute = path.join(base, entry.name);
    const relativePath = path.relative(root, absolute);
    if (isExcluded(relativePath, adapter)) continue;
    if (entry.isDirectory()) {
      await walk(absolute, root, adapter, cutoff, files);
      continue;
    }
    const info = await stat(absolute);
    if (info.mtime < cutoff) continue;
    files.push({
      source: absolute,
      relativePath: relativePath.replaceAll(path.sep, "/"),
      bytes: info.size,
      mtime: info.mtime.toISOString()
    });
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const adapter = getAdapter(args.agent);
  const home = path.resolve(args.home || adapter.defaultHome);
  const now = new Date(args.now || Date.now());
  const cutoff = new Date(now.getTime() - args.retentionDays * 24 * 60 * 60 * 1000);
  const roots = [...adapter.historySources, ...adapter.memorySources];
  const files = [];

  for (const source of roots) {
    await walk(path.join(home, source), home, adapter, cutoff, files);
  }

  const manifest = withProvenance("backup-manifest", {
    agent: adapter.name,
    createdAt: now.toISOString(),
    retentionDays: args.retentionDays,
    dryRun: args.dryRun,
    archivePath: null,
    files,
    excludedPatterns: adapter.exclusions
  }, now);

  if (args.apply) {
    const stamp = args.timestamp || now.toISOString().replace(/[-:]/g, "").replace(/\..+/, "Z");
    const backupDir = path.join(path.resolve(args.outputDir || path.join(home, "backups")), `agent-history-${adapter.name}-${stamp}`);
    await mkdir(backupDir, { recursive: true });
    for (const file of files) {
      const destination = path.join(backupDir, file.relativePath);
      await mkdir(path.dirname(destination), { recursive: true });
      await cp(file.source, destination);
    }
    await writeFile(path.join(backupDir, "manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`);
    process.stdout.write(`${JSON.stringify({ backupDir, files: files.length }, null, 2)}\n`);
  } else {
    process.stdout.write(`${JSON.stringify(manifest, null, 2)}\n`);
  }
}

main().catch(error => {
  console.error(error.message);
  process.exit(1);
});
```

- [ ] **Step 4: Run backup tests**

Run:

```bash
node --test Codex/agent-history-retention/tests/backup.test.mjs
```

Expected: both backup tests pass.

- [ ] **Step 5: Commit**

```bash
git add Codex/agent-history-retention/scripts/agent-history-backup.mjs Codex/agent-history-retention/tests
git commit -m "feat: add cross-agent history backup cli"
```

## Task 6: Add Insights CLI With Tests

**Files:**
- Create: `Codex/agent-history-retention/scripts/agent-history-insights.mjs`
- Create: `Codex/agent-history-retention/tests/insights.test.mjs`
- Create: `Codex/agent-history-retention/templates/candidate-agent-lessons.md`
- Create: `Codex/agent-history-retention/templates/AGENTS.history-lessons.example.md`

- [ ] **Step 1: Add review templates**

Write `Codex/agent-history-retention/templates/candidate-agent-lessons.md`:

```markdown
# Candidate Agent Lessons

These lessons were extracted from local agent history. Review them before copying any lesson into checked-in instructions, Claude settings, Codex memory, or team docs. Do not apply them automatically.

## Preferences

## Repeated Blockers

## Successful Recovery Patterns

## Do Differently Next Time
```

Write `Codex/agent-history-retention/templates/AGENTS.history-lessons.example.md`:

```markdown
# Agent History Lessons Example

Use this as a pattern for human-approved lessons only.

## Durable Lessons

- When a repeated mistake appears in generated insight reports, convert it into a short, testable instruction near the files it affects.
- Keep private transcript evidence out of public repositories.
- Prefer provider-supported settings and local backup policy over undocumented configuration keys.
```

- [ ] **Step 2: Write failing insights test**

Write `Codex/agent-history-retention/tests/insights.test.mjs`:

```js
import assert from "node:assert/strict";
import { mkdtemp, readFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";

const root = path.resolve("Codex/agent-history-retention");
const script = path.join(root, "scripts/agent-history-insights.mjs");
const fixture = path.join(root, "tests/fixtures/codex-home");

test("writes insight artifacts without raw prompts by default", async () => {
  const output = await mkdtemp(path.join(tmpdir(), "agent-history-insights-"));
  const result = spawnSync(process.execPath, [
    script,
    "--agent", "codex",
    "--home", fixture,
    "--since-days", "365",
    "--output-dir", output,
    "--now", "2026-06-27T00:00:00.000Z"
  ], { encoding: "utf8" });

  assert.equal(result.status, 0, result.stderr);
  const summary = JSON.parse(await readFile(path.join(output, "agent-history-insights.json"), "utf8"));
  const markdown = await readFile(path.join(output, "agent-history-insights.md"), "utf8");
  const lessons = await readFile(path.join(output, "candidate-agent-lessons.md"), "utf8");
  assert.equal(summary.promptTextIncluded, false);
  assert.ok(summary.summary.sessions >= 1);
  assert.match(markdown, /Watermark/);
  assert.match(lessons, /Do not apply automatically/);
  assert.doesNotMatch(markdown, /synthetic public fixture/);
});
```

- [ ] **Step 3: Implement insights CLI**

Implement `Codex/agent-history-retention/scripts/agent-history-insights.mjs` so it:

- Reads adapter history sources.
- Parses JSONL line by line with parse-error counting.
- Counts sessions, active days, turns, and project roots.
- Reads memory-like Markdown files when present.
- Extracts lessons from lines containing `preference`, `blocker`, `fix:`, `do differently`, `avoid`, or `when the user`.
- Excludes raw prompt text by default.
- Writes:
  - `agent-history-insights.json`
  - `agent-history-insights.md`
  - `candidate-agent-lessons.md`
- Includes watermark/provenance in all three outputs.

Use this CLI contract:

```bash
node scripts/agent-history-insights.mjs \
  --agent codex \
  --home "$CODEX_HOME" \
  --since-days 365 \
  --output-dir ./out/codex-history-insights
```

- [ ] **Step 4: Run insights tests**

Run:

```bash
node --test Codex/agent-history-retention/tests/insights.test.mjs
```

Expected: insights tests pass and no raw prompt text appears unless `--include-prompts` is passed.

- [ ] **Step 5: Commit**

```bash
git add Codex/agent-history-retention/scripts/agent-history-insights.mjs Codex/agent-history-retention/templates Codex/agent-history-retention/tests/insights.test.mjs
git commit -m "feat: add local agent history insights cli"
```

## Task 7: Add Review And Application Guidance

**Files:**
- Create: `Codex/agent-history-retention/docs/review-and-apply-lessons.md`

- [ ] **Step 1: Add review workflow**

Write `Codex/agent-history-retention/docs/review-and-apply-lessons.md`:

```markdown
# Review And Apply Agent Lessons

Generated lessons are suggestions, not rules.

## Review Checklist

1. Remove any lesson that quotes private prompts, private people, customer names, credentials, internal URLs, or local machine paths.
2. Keep only lessons that are stable across more than one session or clearly important.
3. Rewrite lessons as short, testable instructions.
4. Put team rules in the repository's `AGENTS.md` or equivalent checked-in docs.
5. Put personal preferences in personal instructions or private memory.
6. Keep raw transcript evidence out of public repositories.

## Promotion Targets

| Target | Use For | Public Safe |
|---|---|---|
| `AGENTS.md` | Repo workflow rules and verification commands | Yes, after sanitization |
| Claude project instructions | Claude-specific local work preferences | Usually private |
| Codex memories | Personal recall and recurring preferences | Private by default |
| Repo docs | Community best practices and examples | Yes, with synthetic examples |
| Issue or PR comment | Task-specific lessons from one change | Yes, if sanitized |

## Example Approved Lesson

Raw candidate:

```text
symptom: the agent added unsupported cleanupPeriodDays to Codex config -> cause: Claude and Codex settings were confused -> fix: keep provider-specific settings separate and test config loading.
```

Approved repo instruction:

```markdown
- Keep provider-specific agent settings separate. Do not copy Claude-only settings into Codex config unless Codex documentation supports the key.
```
```

- [ ] **Step 2: Commit**

```bash
git add Codex/agent-history-retention/docs/review-and-apply-lessons.md
git commit -m "docs: add agent lesson review workflow"
```

## Task 8: Add CI And Public Safety Checks

**Files:**
- Create: `.github/workflows/agent-history-retention.yml`

- [ ] **Step 1: Add workflow**

Write `.github/workflows/agent-history-retention.yml`:

```yaml
name: agent-history-retention

on:
  pull_request:
    paths:
      - "Codex/agent-history-retention/**"
      - ".github/workflows/agent-history-retention.yml"
  push:
    branches:
      - main
    paths:
      - "Codex/agent-history-retention/**"
      - ".github/workflows/agent-history-retention.yml"

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - run: node --test Codex/agent-history-retention/tests/*.test.mjs
      - name: public content guard
        run: |
          ! grep -RInE '/U[s]ers/|B[E]GIN .*PRIVATE KEY|sk-[A-Za-z0-9_-]{12,}|t[o]ken=|p[a]ssword=' Codex/agent-history-retention
```

- [ ] **Step 2: Run local equivalent**

Run:

```bash
node --test Codex/agent-history-retention/tests/*.test.mjs
! grep -RInE '/U[s]ers/|B[E]GIN .*PRIVATE KEY|sk-[A-Za-z0-9_-]{12,}|t[o]ken=|p[a]ssword=' Codex/agent-history-retention
```

Expected: tests pass and grep returns no matches.

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/agent-history-retention.yml
git commit -m "ci: validate agent history retention package"
```

## Task 9: Final Release Review

**Files:**
- Inspect: `Codex/agent-history-retention/**`
- Inspect: `README.md`
- Inspect: `Codex/README.md`
- Inspect: `.github/workflows/agent-history-retention.yml`

- [ ] **Step 1: Run full verification**

Run:

```bash
node --test Codex/agent-history-retention/tests/*.test.mjs
rg -n "/U[s]ers/|Oracle confidential|customer data|B[E]GIN .*PRIVATE KEY|sk-[A-Za-z0-9_-]{12,}|t[o]ken=|p[a]ssword=" Codex/agent-history-retention README.md Codex/README.md .github/workflows/agent-history-retention.yml
git diff --check
```

Expected:

```text
tests pass
privacy scan has no matches
git diff --check has no output
```

- [ ] **Step 2: Review source links**

Confirm these source links still resolve:

```text
https://x.com/ArtemXTech/status/2061146280802316741?s=20
https://code.claude.com/docs/en/settings
https://developers.openai.com/codex/config-reference
https://developers.openai.com/codex/config-advanced#config-and-state-locations
https://developers.openai.com/codex/memories
https://developers.openai.com/codex/cli/reference#codex-archive-and-codex-unarchive
https://developers.openai.com/codex/guides/agents-md
https://developers.openai.com/codex/skills
```

- [ ] **Step 3: Open PR**

Use a contribution-focused title:

```bash
git status --short
git log --oneline --max-count=8
gh pr create \
  --title "Add cross-agent history retention and insights best practices" \
  --body "Adds a public-safe community package for local AI-agent history retention, backups, insight extraction, and provenance watermarking across Claude Code, OpenAI Codex, and other agents."
```

## Acceptance Criteria

- Claude users have a documented `cleanupPeriodDays: 365` example.
- Codex users have a supported config example without `cleanupPeriodDays`.
- Other agents can use the adapter contract.
- The package is framed as a run-once local workflow, not a recurring automation.
- The public README names the source improvement link at `https://x.com/ArtemXTech/status/2061146280802316741?s=20`.
- Backup CLI supports dry-run, apply, provider adapters, retention days, output directory, and archive flag.
- Insights CLI writes JSON, Markdown, and review-only candidate lessons.
- Prompt text is excluded by default.
- Every generated artifact includes the standard watermark value from the provenance helper.
- Tests cover privacy exclusions, retention filtering, dry-run no-write behavior, insight extraction, and prompt gating.
- Public docs contain only synthetic examples and public documentation links.
- The contribution explicitly welcomes open source community improvements through pull requests.

## Execution Notes

- Keep commits small and reviewable.
- Do not copy private workstation scripts or transcripts into this public repo.
- Do not publish or push until the public-content checklist passes.
- If provider docs change, update `docs/source-findings.md` before changing examples.
- This is intentionally run once and forgotten. Do not add cron, background services, scheduled transcript harvesting, or continuous monitoring.

## Detailed Reference

### Privacy Contract

- Raw history stays local and private by default.
- Backups are created outside the repository unless the user explicitly provides a private output directory.
- Generated insights are review artifacts only.
- Prompt text is excluded by default.
- Provider auth files, tokens, caches, logs, attachments, shell snapshots, local databases, and temporary files are excluded.
- Public examples use synthetic data only.
- The public package documents the pattern, not any maintainer's private transcripts.

### Source Findings To Preserve

- Public source inspiration: <https://x.com/ArtemXTech/status/2061146280802316741?s=20>. The policy improves that source idea by making it provider-specific, private by default, run-once by design, and open to community pull requests.
- Claude Code documents `cleanupPeriodDays` in `settings.json` as a local cleanup window for old chat transcripts. The community example should show `365` for Claude only.
- OpenAI Codex does not document `cleanupPeriodDays` as a Codex config key. Codex documents `CODEX_HOME`, `config.toml`, `history.jsonl`, session directories, memories, `AGENTS.md`, skills, plugins, and archive/unarchive/delete commands.
- Codex history retention should be implemented through supported Codex settings and local backup policy:

```toml
[history]
persistence = "save-all"

[features]
memories = true

[memories]
generate_memories = true
use_memories = true
```

- Required team behavior belongs in checked-in guidance such as `AGENTS.md`; generated memory or insight files are review inputs, not automatic policy.
- The community project must separate private raw history from public reusable lessons.
