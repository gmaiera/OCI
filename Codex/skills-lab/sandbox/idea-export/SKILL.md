---
name: idea-export
description: "Create a shareable webpage instead of a slide deck to sell, explain, or align people around an idea. Use when the user wants to explore an idea, plan the message, prepare a link or webpage for stakeholders, personalize a page from public or provided context, and end with a clear call to action."
---

# Idea Export

## Purpose

Turn an idea into a persuasive, shareable webpage with a clear audience, message, narrative, proof, and call to action. Prefer an online page or link over a slide deck unless the user explicitly asks for slides.

The page may be general-purpose or person-specific. For person-specific pages, use the target person's public profile URL, supplied photo, and recent public context to make the page relevant to that person's role, operating reality, likely priorities, and decision path.

## Workflow

1. Explore the idea before building.
2. Narrow the message into one audience, one desired decision, and one CTA.
3. Propose the page structure and the deployment or sharing approach.
4. After the user confirms, build the webpage.
5. Verify the page locally, then provide the link or file path.
6. Ask whether the user wants tracking, a form, or a follow-up version.

## Person-Specific Workflow

Use this branch when the user provides a person, profile URL, LinkedIn URL, headshot, or asks to gear a page to a specific stakeholder.

1. Capture the minimum brief:
   - Target person name and preferred nickname.
   - Profile URL or public social URLs, if provided.
   - Attached or local profile image, if provided.
   - Idea or offer to convey.
   - Desired CTA, such as book a session, approve a pilot, reply with feedback, or introduce an owner.
   - Language and tone: personal, executive, technical, commercial, visionary, or informal.
2. Research current public context:
   - If the user asks to look online or provides a profile URL, use web research.
   - Search the provided URL, the person's name, company, role, recent posts, public talks, articles, podcasts, event pages, and company bio pages.
   - Prefer primary/public sources: LinkedIn profile/posts, company pages, conference/session pages, GitHub, personal sites, press releases, or reputable event pages.
   - Capture only public, non-sensitive context. Do not infer private facts, personal attributes, or confidential strategy.
   - If a site blocks direct access, say so and use available public snippets or ask for missing context.
3. Profile image handling:
   - Prefer an image the user attached or supplied locally.
   - If no image is supplied and a public profile image is available, ask before downloading or using it unless the image is clearly intended for public professional use.
   - Store page-specific images under the page's `assets/` folder with descriptive filenames.
4. Draft the personalization:
   - Write for the person's operating context, not just their job title.
   - Mention only facts supported by public sources or the user's provided context.
   - Translate public context into practical relevance: priorities, customer segment, region, team cadence, decisions, risks, or opportunities.
   - Keep the page warm and direct; avoid overclaiming, flattery, or surveillance-like phrasing.
5. Build the page:
   - Clone an existing page only when it is a strong fit and then remove leftover references.
   - Update title, meta description, hero, image alt text, console/debug labels, CTA, footer, and copyable response or scheduling link.
   - Run text searches for the previous person's name, image filename, and old CTA wording before publishing.
6. Publish:
   - Publish only approved public artifacts to the chosen hosting target.
   - Ask before publishing if the content includes sensitive, internal, or unapproved details.
7. Verify:
   - Confirm the page loads.
   - Confirm key assets load, especially profile image and CSS.
   - Fetch the live or local HTML and verify the new title and CTA are present.

## Discovery Questions

Ask only what is needed. Use the answers to form a concise brief:

- Who is the audience?
- If person-specific: what is the person's name, profile URL, preferred nickname, and relationship to the user?
- What should they understand, believe, decide, or do after reading?
- What pain, opportunity, or change creates urgency?
- What proof, examples, numbers, stories, or references support the idea?
- What objections or risks should the page answer?
- What exact CTA should appear at the end?
- How should the audience respond: email, form, calendar link, chat, GitHub issue, survey, or another channel?
- Should the tone be executive, visionary, technical, commercial, educational, or personal?

## Page Pattern

Use this structure unless the idea calls for a different one:

1. Hero: clear title, one-line promise, primary CTA.
2. Why now: context, problem, timing, or opportunity.
3. The idea: explain the proposal in plain language.
4. What changes: before/after or current/future state.
5. Proof: data, examples, references, mockups, quotes, or demos.
6. Plan: simple next steps, responsibilities, timeline, or first-version path.
7. Risks and safeguards: acknowledge concerns and show mitigation.
8. CTA: ask for one concrete response or decision.

## CTA Rules

Make the final CTA impossible to miss and easy to answer. Prefer one primary action:

- "Approve the V1 experiment"
- "Reply with yes/no and one concern"
- "Choose one of these three options"
- "Book a 30-minute alignment session"
- "Add comments directly in this form"
- "Nominate one owner for the next step"

When useful, include a secondary low-friction action such as "send one objection" or "share with one stakeholder."

For scheduling CTAs, prefer an external booking link such as Microsoft Bookings, Outlook booking page, Calendly, or a calendar scheduling URL. Static pages should link out to scheduling rather than handling OAuth or calendar availability itself.

## Build Guidance

- Build an actual webpage, not a landing-page explanation about the process.
- Keep the first viewport focused on the idea and decision, not a marketing splash.
- Use restrained, professional design for enterprise or stakeholder alignment pages.
- Use visual assets when they clarify the idea: diagrams, screenshots, icons, simple charts, or generated imagery.
- For person-specific pages, use the person's image only when the user supplies it, approves it, or it is clearly public professional imagery appropriate for the intended audience.
- Avoid card-heavy decorative layouts when the page is for executives or operational stakeholders.
- Make the page easy to scan in 60 seconds and persuasive in 5 minutes.
- Include a visible response mechanism in the CTA section.

## Link And Deployment Options

Choose the simplest option that fits the situation:

- Local preview: static HTML file when the user only needs to review or send internally later.
- Local dev server: use for apps or pages with build tooling.
- Existing repo/site: add the page under the project if there is an established deployment path.
- Public/shareable hosting: use the user's preferred hosting workflow when available; ask before deploying externally.

Before deploying publicly, confirm whether the content is confidential, internal-only, or safe to share.

## Output

When done, provide:

- The page link or local file path.
- A one-paragraph summary of the message.
- The exact CTA used.
- For person-specific pages, a brief note on what public context shaped the personalization.
- Any assumptions or unresolved questions.
