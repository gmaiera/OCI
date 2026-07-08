# DeepResearch Reference

Read this file for a Full report, disputed evidence, comparisons, or a reusable evidence ledger. Adapt the modules to the user's requested format; do not force every section.

## Evidence Ledger

Repeat rows until every research sub-question is answered, unresolved, or out of scope.

| Sub-question | Material claim | Source of record | Independent corroboration | Contradiction | Source date/class | Incentives or limitations | Evidence strength |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Record direct links or environment-native citations in the source cells. Treat syndicated copies and reports derived from the same underlying dataset as one evidence chain.

## Claim-Relative Source Assessment

| Source class | What it can establish | Typical limitation |
|---|---|---|
| Official documentation, filing, regulator, standard, code, court record | Exact published fact, rule, behavior, or recorded event | May not establish effectiveness, adoption, or comparative superiority |
| Company announcement or investor material | What the organization claims, offers, or announced | Self-interested; independently corroborate performance, customers, market position, and forecasts |
| Peer-reviewed research | Methods and findings within the studied conditions | May be narrow, old, non-replicated, or inapplicable operationally |
| Preprint or vendor benchmark | Early technical evidence | Not peer reviewed or independently designed; label methodology and sponsor |
| Independent reputable reporting | Corroboration, context, stakeholder perspectives | May rely on anonymous or shared upstream sources |
| Expert commentary | Interpretation and domain context | Opinion; disclose affiliation and incentives |
| Social/community evidence | Leads, sentiment, operational weak signals | Not verification unless confirmed elsewhere |
| Patent | Filing and claims | Not proof of implementation, validity, commercial use, or product intent |

## Evidence Strength Labels

Apply the first matching rule to the exact claim, then stop:

1. **Contested**: Two or more credible evidence chains materially conflict on the exact claim. State the disagreement and what would resolve it.
2. **Unknown**: No source directly supports the exact claim after a proportionate search. Identify the missing evidence or follow-up.
3. **Verified**: Direct source-of-record evidence establishes the exact bounded claim and, for a consequential, disputed, adverse, performance, or self-interested claim, appropriate independent corroboration also supports it. A source is a source of record for its own existence and contents, not for the truth of substantive claims it merely asserts.
4. **Weak signal**: One or more sources directly support the exact substantive claim, but every supporting evidence chain is preliminary, unreviewed, sponsor-controlled, social/community, or methodologically insufficient.
5. **Supported**: At least one credible direct evidence chain is stronger than a Weak signal, no credible evidence materially conflicts, and the claim does not meet the Verified rule.

Classify source existence separately from source content. For example, a preprint's existence can be **Verified** while its reported effect remains a **Weak signal** and an unevidenced commercial implementation remains **Unknown**.

For a proof-or-implementation question involving preliminary research or patent evidence, report three separately labeled claims: source existence or filing (**Verified** when the direct source establishes it), the reported result (**Weak signal** while preliminary or methodologically insufficient), and implementation or commercial use (**Unknown** without direct product or deployment evidence).

## Full-Report Scaffold

```markdown
# [Decision or topic]

**Research current as of:** [date]

## Conclusion
[Answer and decision implication in 2-4 sentences.]

## Key findings
- [Material claim with adjacent citation.]

## Evidence, uncertainty, and contradictions
- **Verified:** ...
- **Supported / Contested / Weak signal / Unknown:** ...

## Recommendation
[Action, rationale, first step, time horizon, and confidence. Include only when the request is decision-oriented.]
```

Conditional modules: scope and method, timeline, comparison, risks, opportunities, regional analysis, implementation plan, or selected sources.

## Comparison Module

```markdown
| Aspect | Option A | Option B | Evidence-backed takeaway |
|---|---|---|---|
| | | | |
```

Cite factual cells or the takeaway immediately. Compare only dimensions relevant to the decision.

## Opportunity Module

```markdown
1. **[Opportunity]**
   - Why it matters:
   - Who can act:
   - First step:
   - Time horizon:
   - Evidence strength:
```

## Research-As-Of And Data-Gap Language

Use only the evidence-strength labels defined above. Add these phrases after a label when useful:

- **Current as of [date]**: defines the evidence cutoff, not a guarantee that no later event exists.
- **Supported — independent corroboration missing**: credible non-preliminary evidence supports the claim and is stronger than a Weak signal, but independent confirmation needed for Verified status was not found.
- **Searched but not found**: name the source classes and date range checked when the gap matters.
- **Could change the conclusion**: identify the exact missing fact, threshold, or event.
