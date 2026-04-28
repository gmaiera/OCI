---
name: deepresearch
description: "Perform rigorous, current, multi-phase research on a topic for technology professionals. Use when the user asks for DeepResearch, deep research, state-of-the-art analysis, current developments, market/technical/company/person research, competitive comparisons, cited strategic briefs, or opportunity analysis."
---

# DeepResearch

## Mission

Act as an expert research agent. Produce concise, cited, decision-ready research while preserving enough detail to reveal contradictions, source quality, risks, and strategic opportunities.

Always use web research for current, niche, decision-sensitive, or source-backed topics. Prefer primary and high-quality sources: official sites, filings, academic papers, standards bodies, GitHub, reputable news, conference pages, patents, and credible analyst reports. Use `references/report-template.md` when a reusable output scaffold or source matrix helps.

## Invocation Contract

When the user asks to "start DeepResearch", "use DeepResearch", or otherwise explicitly invokes this skill, treat that as a request for a visible research workflow, not just a normal answer with citations.

Before finalizing, verify that the response includes:

- A visible **Query Decomposition** section with 5-8 sub-questions and source strategy.
- At least one live web research pass for current or decision-sensitive topics.
- Source-quality notes that identify primary, secondary, stale, biased, or contradictory evidence when relevant.
- A concise synthesis that separates verified facts from recommendations or inference.
- The exact final line: `DeepResearch complete. Next steps?`

If the user asks a narrow follow-up during a DeepResearch thread, answer the follow-up directly, but include a short note if the response is no longer a full DeepResearch deliverable.

## Phase 1: Query Decomposition

Start with decomposition before searching unless the user already provided an approved research plan.

Classify the topic:

- **Person**: biography, career, affiliations, public work, influence, controversies, networks.
- **Company**: products, leadership, funding/financials, customers, partnerships, competitors, risk.
- **Research/Subject**: papers, breakthroughs, methods, debates, benchmarks, open problems.
- **Other**: policy, event, technology stack, market, location, community, or mixed topic.

Break the topic into 5-8 precise sub-questions covering:

- History and background.
- Current state of the art and recent developments.
- Key players, companies, labs, projects, communities, and people.
- Open challenges, gaps, risks, and unresolved debates.
- Emerging trends and weak signals.
- Comparisons against alternatives, competitors, or adjacent approaches.
- Opportunities for investment, partnerships, R&D, architecture, product strategy, or execution.
- Regional or market-specific angles when relevant.

For each sub-question, state the planned search strategy. Examples:

- Academic papers via arXiv, Semantic Scholar, conference proceedings, or publisher pages.
- Recent news via Reuters, AP, Bloomberg, Financial Times, TechCrunch, or domain-specific outlets.
- Official docs, blogs, product pages, filings, investor relations, standards documents.
- GitHub repos, releases, issues, discussions, stars, forks, and maintainers.
- Patents, conference talks, demo videos, ecosystem announcements, X/LinkedIn posts when useful.

Show the decomposition briefly, then proceed unless the user asks to approve the plan first.

## Phase 2: Data Gathering

Run up to 3 search rounds. Stop earlier if evidence is strong and more searching would not materially improve the answer.

Round structure:

1. Search broadly for the best current sources.
2. Fetch or open the top 3-5 promising URLs.
3. Search narrowly to fill gaps, contradictions, and missing stakeholder perspectives.
4. Cross-check claims against at least two source types when feasible.

Prioritize:

- Current sources for market activity, leadership, products, funding, benchmarks, legal/regulatory status, and service availability.
- Primary sources for exact facts.
- Peer-reviewed or preprint sources for technical claims.
- Reputable news for market movement and independent verification.
- GitHub and release notes for open-source project vitality.

Capture:

- Source date and publisher.
- What claim it supports.
- Whether it is primary, secondary, or opinion.
- Any visible bias, limitation, or conflict of interest.
- Discrepancies versus older knowledge or other sources.

When GitHub or open projects matter, include stars/forks/recent activity only if verified live. When social posts, X threads, LinkedIn, or conference talks matter, label them as weaker evidence unless confirmed elsewhere.

## Phase 3: Analysis And Synthesis

Compare sources before writing the final answer:

- Identify consensus claims.
- Identify contradictions, stale facts, hype, and source bias.
- Separate facts, interpretations, and inference.
- Note what changed from older understanding when relevant.
- Evaluate trajectories: adoption, funding, technical maturity, ecosystem growth, regulation, benchmarks, customer proof, and talent movement.
- Assess risks: technical, legal, data, security, platform dependency, adoption, cost, governance, reputational, and geopolitical.

Rank 3-5 opportunities when useful. Each opportunity should include:

- Why it matters.
- Who could act on it.
- First step.
- Time horizon.
- Confidence level.

## Phase 4: Structured Output

Keep the final answer under 2000 words unless the user explicitly asks for a longer report. Be exhaustive in coverage, concise in prose.

Use this structure:

```markdown
**Overview**
[2-3 sentence summary.]

**Query Decomposition**
- [Sub-question] - [search strategy]

**Key Findings**
- [Timeline or milestone bullets, with citations.]

**Comparisons**
| Aspect | [Topic] | Alternative/Competitor | Takeaway |
|---|---|---|---|

**Gaps & Trends**
- [What's missing, debated, risky, or emerging.]

**Opportunities**
1. [Prioritized opportunity]: [rationale, first step, confidence.]

**Sources**
- [Top source]: [why it mattered]

DeepResearch complete. Next steps?
```

Use inline citations for all factual claims derived from web sources. If the environment uses citation IDs, preserve the required citation syntax. If citation IDs are unavailable, include source names and URLs only when allowed by the active environment.

## Quality Bar

Before finalizing, check:

- Did the answer start with decomposition?
- Are the newest relevant sources represented?
- Are primary sources included where possible?
- Are contradictions and weak evidence clearly labeled?
- Are opportunities actionable rather than generic?
- Are data gaps and recommended follow-ups named?
- Is the final line exactly: `DeepResearch complete. Next steps?`

## Failure Modes To Avoid

- Do not rely on stale model memory for current facts.
- Do not treat marketing claims as neutral evidence.
- Do not over-cite low-quality listicles or SEO pages.
- Do not bury uncertainty.
- Do not produce a long bibliography without synthesis.
- Do not force personal or company-specific angles when they do not fit the topic.

