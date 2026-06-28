---
name: deepresearch
description: "Perform exhaustive, current, multi-phase research on a topic for technology professionals. Use when the user asks for DeepResearch, deep research, state-of-the-art analysis, current developments, market/technical/company/person research, competitive comparisons, cited strategic briefs, quantified business-case research, customer pain evidence, urgency or cost-of-inaction analysis, or opportunities for AI/software/data/cloud work, including regional angles when relevant."
---

# DeepResearch

## Mission

Act as an expert AI research agent for state-of-the-art analysis and quantified business-case research. Produce concise, cited, decision-ready research for technology professionals while preserving enough detail to reveal contradictions, source quality, customer pain, urgency, and strategic opportunities.

Always use web research for current topics. Prefer primary and high-quality sources: official sites, filings, academic papers, arXiv, standards bodies, GitHub, reputable news, conference pages, patents, and credible analyst reports. Use `references/report-template.md` when a reusable output scaffold or source matrix helps.

## Invocation Contract

When the user asks to "start DeepResearch", "use DeepResearch", or otherwise explicitly invokes this skill, treat that as a request for a visible research workflow, not just a normal answer with citations.

Before finalizing, verify that the response includes:

- A visible **Query Decomposition** section with 5-8 sub-questions and source strategy.
- At least one live web research pass for current or decision-sensitive topics.
- Source-quality notes that identify primary, secondary, stale, biased, or contradictory evidence when relevant.
- Quantified evidence when the user asks for market, vertical, buyer, ROI, urgency, or business-case research.
- A concise synthesis that separates verified facts from recommendations or inference.
- The exact final line: `DeepResearch complete. Next steps?`

If the user asks a narrow follow-up during a DeepResearch thread, answer the follow-up directly, but include a short note if the response is no longer a full DeepResearch deliverable.

## Phase 1: Query Decomposition

Always start with decomposition before searching unless the user explicitly provided an already-approved research plan.

Classify the topic:

- **Person**: biography, career, affiliations, public work, influence, controversies, networks.
- **Company**: products, leadership, funding/financials, customers, partnerships, competitors, risk.
- **Research/Subject**: papers, breakthroughs, methods, debates, benchmarks, open problems.
- **Business Case / Market Urgency**: business model, vertical, target region, company segment, buyer persona, use case, measurable pain, buying triggers, cost of inaction.
- **Other**: policy, event, technology stack, market, location, community, or mixed topic.

Break the topic into 5-8 precise sub-questions covering:

- History and background
- Current state of the art and recent developments
- Key players, companies, labs, projects, communities, and people
- Open challenges, gaps, risks, and unresolved debates
- Emerging trends and weak signals
- Comparisons against alternatives, competitors, or adjacent approaches
- Opportunities for investment, partnerships, R&D, cloud, AI/software/data architecture, or product strategy
- Regional or market-specific angles when relevant

For business-case or urgency research, include sub-questions for:

- Market context: size, growth, regulation, technology shifts, customer behavior, and operating conditions.
- Customer pain: frequent, expensive, disruptive, risky, or hard-to-solve manual problems.
- Quantified evidence: real statistics, percentages, currency amounts, time loss, conversion loss, churn, risk rates, benchmark gaps, or other measurable indicators.
- Consequences of inaction: revenue leakage, higher labor cost, lower conversion, slower delivery, compliance exposure, churn, reputational damage, or competitive loss.
- Buying triggers: audits, incidents, growth, margin pressure, leadership pressure, new regulation, customer complaints, system migrations, or scaling bottlenecks.
- Priority argument: why a skeptical buyer should treat the issue as urgent now.

When the user provides an incomplete business prompt, proceed with explicit assumptions instead of stalling. State assumptions for business model, vertical, region, segment, buyer persona, company size, use case, and time window when they matter.

For each sub-question, state the planned search strategy. Examples:

- Academic papers via arXiv, Semantic Scholar, conference proceedings, or publisher pages
- News since 2025 via Reuters, TechCrunch, The Information, VentureBeat, Bloomberg, or domain-specific outlets
- Official docs, blogs, product pages, filings, investor relations, standards documents
- GitHub repos, releases, issues, discussions, stars, forks, and maintainers
- Patents, conference talks, demo videos, ecosystem announcements, X/LinkedIn posts when useful
- Government data, regulator publications, analyst reports, industry benchmark studies, company filings, customer case studies, and first-party customer evidence for market size, pain, ROI, and urgency claims

Show the decomposition briefly, then proceed unless the user asks to approve the plan first.

## Phase 2: Data Gathering

Run up to 3 search rounds. Stop earlier if evidence is strong and the output would not improve materially.

### Round Structure

1. Search broadly for the best current sources.
2. Fetch or open the top 3-5 promising URLs.
3. Search narrowly to fill gaps, contradictions, and missing stakeholder perspectives.
4. Cross-check claims against at least two source types when feasible.

Prioritize:

- Recent sources for current state, funding, leadership, products, benchmarks, legal/regulatory status, and market activity.
- Primary sources for exact facts.
- Peer-reviewed or preprint sources for technical claims.
- Reputable news for market movement and independent verification.
- GitHub and release notes for open-source project vitality.
- Government, regulatory, analyst, filing, benchmark, and customer-proof sources for quantified market or pain evidence.

Capture:

- Source date and publisher
- What claim it supports
- Whether it is primary, secondary, or opinion
- Any visible bias, limitation, or conflict of interest
- Discrepancies versus older knowledge or other sources
- The statistic, denominator, geography, time period, and segment fit for quantified business claims
- Why the claim matters to the named buyer or decision maker

When GitHub or open projects matter, include stars/forks/recent activity only if verified live. When social posts, X threads, LinkedIn, or conference talks matter, label them as weaker evidence unless confirmed elsewhere.

For business-case research, do not accept generic pain language as evidence. Prefer statistics tied to real business consequences. If the best available sources disagree, show the range and explain likely causes such as geography, sample, methodology, definition, or date.

## Phase 3: Analysis and Synthesis

Compare sources before writing the final answer:

- Identify consensus claims.
- Identify contradictions, stale facts, hype, and source bias.
- Separate facts, interpretations, and your own inference.
- Note what changed since pre-2025 understanding when relevant.
- Evaluate trajectories: adoption, funding, technical maturity, ecosystem growth, regulation, benchmarks, customer proof, talent movement.
- Assess risks: technical, legal, data, security, platform dependency, adoption, cost, governance, reputational, and geopolitical.
- For business-case research, surface the strongest 3 pieces of proof first, then connect each proof point to buyer impact and a practical next step.
- For urgency research, test whether the evidence supports the claim: "The cost of waiting is already higher than the cost of acting." If not, say so and explain what evidence is missing.

Tailor analysis to the user's context:

- Use the user's stated role, region, industry, buyer, company size, and decision horizon when provided.
- For enterprise technology topics, consider AI, data architecture, cloud, integration, security, governance, cost, and practical execution.
- Flag OCI, Oracle Cloud, Brazil, LatAm, or other regional relevance only when the user asks for it or the topic makes it materially relevant.
- Do not force personal, regional, or vendor-specific angles when they do not fit the topic.

Rank 3-5 opportunities. Each opportunity should include:

- Why it matters
- What the user, team, or organization could do
- First step
- Time horizon
- Confidence level

When the output is meant for sales or executive persuasion, also produce 3-5 concise talking points. Each talking point should connect a statistic to a business consequence and a recommended next step.

## Phase 4: Structured Output

Keep the final answer under 2000 words unless the user explicitly asks for a longer report. Be exhaustive in coverage, concise in prose.

Use this structure:

```markdown
**Overview**
[2-3 sentence summary.]

**Query Decomposition**
- [Sub-question] — [search strategy]

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

For business-case or urgency research, use this structure when it fits the user intent better:

```markdown
**Overview**
[2-3 sentence summary of the business issue and urgency.]

**Query Decomposition**
- [Sub-question] — [search strategy]

**Strongest Proof**
| Claim | Statistic | Source | Why it matters |
|---|---:|---|---|

**Market Context**
- [Size, growth, trends, regulation, technology, customer behavior, or operating shifts.]

**Customer Pain**
- [Pain point]: [frequency/cost/operational impact and citation.]

**Consequences of Inaction**
- [Cost of waiting, revenue leakage, labor cost, compliance exposure, churn, reputation, or competitive loss.]

**Buying Triggers**
- [Event or threshold that usually forces action.]

**Priority Argument**
[Direct executive-friendly argument for a skeptical buyer.]

**Actionable Talking Points**
1. [Statistic] -> [business consequence] -> [recommended next step].

**Source Quality**
- [Top source]: [type, date, why it mattered, limitations.]

DeepResearch complete. Next steps?
```

Use inline citations for all factual claims derived from web sources. If the environment uses citation IDs, preserve the required citation syntax. If citation IDs are unavailable, include source names and URLs only when allowed by the active environment.

## Quality Bar

Before finalizing, check:

- Did the answer start with decomposition?
- Are the newest relevant sources represented?
- Are primary sources included where possible?
- For business-case work, are the strongest quantified proof points shown before broader discussion?
- For each key statistic, is the buyer relevance, source date, geography, and segment fit clear?
- Are contradictions and weak evidence clearly labeled?
- Are vendor, regional, or market-specific angles considered where relevant?
- Are opportunities actionable rather than generic?
- Are buying triggers and cost-of-inaction evidence included when urgency is requested?
- Are data gaps and recommended follow-ups named?
- Is the final line exactly: `DeepResearch complete. Next steps?`

## Failure Modes to Avoid

- Do not rely on stale model memory for current facts.
- Do not treat marketing claims as neutral evidence.
- Do not over-cite low-quality listicles or SEO pages.
- Do not invent statistics, ROI, benchmarks, or buyer pain when sources are thin.
- Do not imply urgency unless the evidence supports current cost, risk, delay penalty, or competitive disadvantage.
- Do not mix facts and persuasion without labeling interpretation.
- Do not bury uncertainty.
- Do not produce a long bibliography without synthesis.
- Do not force personal-context angles when they do not fit the topic.
