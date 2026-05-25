What This Skill Does
Takes a single "[X] vs [Y]" keyword as input. Outputs a complete, publish-ready
HTML page that:

Ranks on Google for that keyword
Gets cited by AI tools like ChatGPT and Perplexity (schema + clear structure)
Converts readers into newsletter subscribers or tool users
Sounds like a human wrote it — not a content farm

This skill was built from a real reference page: windsurf-vs-cursor-reddit.html.
Every decision in that page is the rule for all future pages.

Step 0 — Before You Write Anything
Run these three searches. Do not skip. Pages built without fresh data get
outranked fast because pricing, features, and community opinion change monthly.
Search 1: "[X] vs [Y] reddit [current year]"
Search 2: "[X] vs [Y] pricing [current year]"
Search 3: "[X] vs [Y] honest review developer experience"
Pull from results:

Current pricing for both tools (exact numbers, not ranges)
2–3 genuine community quotes (Reddit, dev forums, real reviews)
Any recent product changes (acquisitions, new models, new features)
One benchmark or performance stat if available

If search returns nothing useful on one of the tools — say so in the page.
"We couldn't find recent benchmarks for X" is better than invented data.

Tone Rules — Non-Negotiable
Every sentence must pass these filters before it stays in the page:
DO:

Short sentences. Max 20 words per sentence as a target.
Active voice. "Cursor wins on speed" not "Speed is where Cursor has been found to excel."
Specific claims. "Cursor is $20/month" not "Cursor is competitively priced."
Honest verdicts. If both tools are mediocre for a use case, say that.
Real community voice. Pull actual Reddit phrasing. Don't sanitize it into corporate speak.

DO NOT:

"In the ever-evolving landscape of..." — delete on sight
"Both tools offer robust..." — meaningless
"Ultimately, the best tool depends on your needs" — this is the refuge of writers who have no opinion
Bullet lists of features without a verdict on each
Any sentence that could appear in a press release

The test: Read each paragraph out loud. If it sounds like something a product marketing manager wrote, rewrite it. If it sounds like a developer explaining to a friend over coffee, keep it.

Page Architecture — Follow This Exactly
Every page has these 9 sections in this order. Do not add sections.
Do not remove sections. The structure is the template.
1. <head>          — Meta, OG, schema, fonts, CSS
2. Hero            — Title, subtitle, meta row (date, read time)
3. TOC             — Anchor links to all 7 content sections
4. Quick Verdict   — The answer in 30 seconds. Two verdict cards.
5. Reddit Says     — 3 community quotes with thread attribution
6. Head-to-Head    — Comparison table, 8–10 rows
7. Pricing         — Three price cards: Tool X / Tool Y / Team Tier
8. Scenarios       — 6 scenario cards: 3 pick X, 3 pick Y
9. The Third Option — Your unique angle + conversion CTA
10. FAQ            — 5–6 questions with direct answers
11. Footer
The page ends with FAQ then footer. The CTA lives inside section 9 —
"The Third Option" — not at the very end as a tacked-on block.

Section-by-Section Writing Instructions
Section 1: <head>
Copy this block exactly and fill in the blanks:
html<title>[X] vs [Y]: What [Community/Reddit] Actually Says in [YEAR]</title>
<meta name="description" content="We compiled real [community] opinions comparing
[X] vs [Y] — no marketing copy. Honest pricing breakdown, speed comparison, and
a clear answer on which to pick." />
<link rel="canonical" href="https://yourdomain.com/[url-slug]" />
JSON-LD: Always include both Article and FAQPage schema types.
The FAQPage answers must match the actual FAQ section content exactly —
Google cross-checks these.
json{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "[TITLE]",
      "datePublished": "[ISO DATE]",
      "dateModified": "[ISO DATE]"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "[Question from FAQ section]",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "[Exact answer from FAQ section]"
          }
        }
      ]
    }
  ]
}

Section 2: Hero
Title formula: [X] vs [Y]: [What Community] Actually Says in [YEAR]
Subtitle: One paragraph, 2–3 sentences max. State what makes this page
different from every other comparison article. Name the thing you did
(searched Reddit, ran both tools on a real project, compiled 40 threads)
so the reader knows within 5 seconds why they should keep reading.
Meta row must show: Author name · Publish date · Read time · "Pricing verified [Month Year]"
The "Pricing verified" tag is important. It signals freshness to both readers
and Google.

Section 3: Quick Verdict
Two verdict cards side by side. No prose before the cards — go straight to them.
Card format:
[Tool Name]  [one-word positioning badge]
[2–3 sentence verdict. What it's best at. Who it's for. One honest limitation.]
The verdict must take a position. "Both are good depending on your needs" is
not a verdict. Pick a winner per use case and say it.

Section 4: What Reddit / Community Actually Says
Three subsections:

On [main technical difference — e.g., Speed vs Depth]
On [second debate — e.g., "The Just Use Both Camp"]
On [developer experience / trust / daily feel]

Each subsection: 1–2 sentences of your framing, then 1 reddit-quote block.
Reddit quote block format:
html<div class="reddit-quote">
  <blockquote>[Quote — paraphrased if needed, but keep the voice raw]</blockquote>
  <div class="thread-info">r/[subreddit] · [context] · [year]</div>
</div>
End section 4 with a callout box. The callout delivers the meta-insight —
what the pattern across all these threads actually reveals. This is where
you say the thing most articles won't say.

Section 5: Head-to-Head Table
8–10 rows. Each row is a real decision-making criterion, not a feature spec.
Row format: Criterion | [X] value | [Y] value
Mark winners with ✓ prefix and .win class. Mark losers with .lose class.
Rules for the table:

No row where both tools tie — pick a winner or explain the tradeoff
Pricing must be exact numbers from your search (not "starting at")
At least one row where the "expected winner" loses (surprises build trust)
The last row should be something subjective: "Day-one usability" or
"Who it's actually built for" — end on human terms, not specs


Section 6: Pricing
Three price cards:

[Tool X] Pro / Individual
[Tool Y] Pro / Individual
Teams Tier — show both side by side in one card

The card with the better value gets the .featured class (green border).
After the cards: one paragraph on what "price parity" or "price difference"
actually means in practice. Don't just list numbers — explain the implication.
Example: "At the individual level, the pricing is identical. That means the
decision is entirely about what you get — not what you pay."

Section 7: Scenarios
6 scenario cards in a 2-column grid.
3 cards say "Pick [X]". 3 cards say "Pick [Y]".
They alternate: X, Y, X, Y, X, Y.
Each card: one concrete situation. One paragraph explaining why that tool
fits. No bullet points inside the card.
The situations must be specific:

Bad: "You work on large projects"
Good: "You're working on a codebase with 10+ files, multiple modules,
or inherited code you didn't write"


Section 8: The Third Option
This is the most important section. It's where you convert.
Structure:

Name what the whole debate is really about underneath the surface.
The X vs Y fight is a symptom. What's the actual problem?
State that neither tool fully solves it.
Introduce your solution — not as an ad, but as the logical next step
given what you just explained.
CTA block — email signup with a specific value promise.

CTA block rules:

The value promise must be specific: "We test 3 AI tools every week and
report what's actually worth your time" not "Get AI news in your inbox"
Social proof number if you have it: "Join 4,200+ developers"
One field only: email. No name field. No dropdown.
Button text is action + outcome: "Get the Weekly Verdict →"
not "Subscribe" or "Sign Up"


Section 9: FAQ
5–6 questions. Each answer is 2–5 sentences. Direct. No hedging.
Good FAQ questions follow these patterns:

"Is [X] actually better than [Y] in [YEAR]?" — give a real answer
"What does Reddit say about switching from [X] to [Y]?"
"Can I use [X] with [specific popular tool/IDE/language]?"
"Are there free tiers for either?" — pricing reality check
"What happened to [X/Y] — [recent news question]?" — shows freshness
"Should I use [X] or [Y] for [specific tech stack]?" — practical case

FAQ answers must match the JSON-LD schema answers exactly.
Same wording. Google checks this.

CSS Variables — Use These Exact Names
The CSS system uses these token names. Keep them consistent across every page
so future batch updates are one find-and-replace:
css:root {
  --bg         /* page background */
  --surface    /* card / section backgrounds */
  --border     /* subtle borders */
  --border2    /* stronger borders */
  --text       /* body text */
  --muted      /* secondary text, metadata */
  --accent     /* primary action color */
  --accent2    /* secondary accent (inline CTAs) */
  --heading    /* h1, h2, h3 color */
  --mono       /* monospace font stack */
  --serif      /* display font stack */
  --sans       /* body font stack */
  --radius     /* border-radius base */
  --max        /* content max-width (760px) */
}
Current color theme (white background):
css--bg: #ffffff
--surface: #f5f6fa
--border: #e2e5ef
--border2: #c9cede
--text: #3a3d4d
--muted: #7a7f9a
--accent: #0a7c4e
--accent2: #5b47e0
--heading: #0f1117
To switch to dark theme, swap these values. Every component references
the variable, so nothing else needs to change.

Component Classes — Required in Every Page
These class names must appear in every generated page. They are the design
system. Do not rename them.
.topbar           — site header bar
.hero             — page hero section
.category-tag     — small label above h1
.verdict-box      — quick verdict container
.verdict-grid     — 2-col grid inside verdict-box
.verdict-card     — individual tool card
.reddit-quote     — community quote block
.compare-table-wrap — scrollable table wrapper
.callout          — highlighted insight box
.scenario-grid    — 2-col scenario grid
.scenario-card    — individual scenario
.sc-badge         — "Pick Cursor" / "Pick Windsurf" label
.badge-[toolname] — tool-specific badge color
.pricing-row      — 3-col pricing grid
.price-card       — individual price card
.price-card.featured — highlighted price card
.cta-block        — main conversion section
.cta-form         — email form inside CTA
.inline-cta       — mid-article conversion nudge
.faq-item         — individual FAQ row
.faq-q / .faq-a   — question / answer typography
.win / .lose      — table cell winners/losers
#progress         — reading progress bar (fixed)

Slug and URL Formula
Pattern: /[tool-x]-vs-[tool-y]-[community-modifier]
Examples:

/windsurf-vs-cursor-reddit
/chatgpt-vs-claude-business-emails
/jasper-vs-copyai-marketing-teams
/notion-ai-vs-mem-knowledge-workers

Rule: If the keyword includes "reddit" — keep it in the slug.
Reddit-modified keywords have distinct search intent and shouldn't be
canonicalized away from the intent signal.

What Changes Per Page vs What Never Changes
Changes every page (swap these out):

Tool names throughout (X and Y)
Tool descriptions and verdicts
All pricing (run fresh search every time)
Community quotes (find tool-specific threads)
Comparison table rows and winners
Scenario card situations
FAQ questions and answers
JSON-LD schema content
Meta title, description, canonical URL
Slug

Never changes (copy as-is):

Full CSS block
Page architecture (9 sections, same order)
Font imports
Component class names
CTA structure and email form logic
Progress bar script
Footer structure
Tone rules


Quality Checklist — Run Before Finalizing
Before outputting the page, verify:
Data:

 Both tool prices sourced from a search run today (not from memory)
 At least 2 community quotes with subreddit and approximate date
 One product update or news item from the last 6 months mentioned
 Comparison table has at least 8 rows with real winners picked

Tone:

 Zero sentences starting with "In today's..."
 Zero uses of "robust", "seamless", "leverage", "innovative"
 Every table row has a clear winner or explicit tradeoff stated
 The Third Option section names the real problem, not just pitches the product

Technical SEO:

 <title> under 60 characters
 Meta description under 160 characters
 Canonical URL set
 FAQPage schema answers match FAQ section word-for-word
 datePublished and dateModified set to today's date
 All section IDs match TOC anchor links

Conversion:

 CTA is in section 8 (Third Option), not bolted to the footer
 Inline CTA appears once, mid-article, after the comparison table
 Email button text is specific (not "Subscribe")
 fetch('/api/subscribe', ...) line is present and commented with TODO


Example: Good vs Bad Writing
BAD (do not write like this):

"Both Windsurf and Cursor are innovative AI-powered development environments
that offer robust features for modern developers. Ultimately, the best choice
depends on your specific workflow requirements and team structure."

Why it's bad: No verdict. No specifics. Every word could describe any two tools.
This sentence could have been written by someone who has never used either tool.

GOOD (write like this):

"Cursor is faster. Windsurf understands more. Those two facts explain 80% of
the debate. If you're deep in a 500-file codebase you didn't write, Windsurf's
Cascade agent will save you more time. If you're building a new feature from
scratch and want AI that gets out of your way, Cursor wins."

Why it's good: Makes a claim. Explains it with a specific mechanism (Cascade agent,
file count). Gives two concrete scenarios. Reader can immediately map it to their situation.

BAD Reddit quote framing:

"Community members have noted that Windsurf performs admirably in complex
codebase scenarios."

Why it's bad: This is not how developers talk. The voice is sanitized into uselessness.

GOOD Reddit quote framing:

Developers on r/ChatGPTCoding are pretty direct about it:

"Windsurf edged out better with a medium to big codebase — it understood the context
better. For quick patches though, Cursor is just faster to get out of your way."

That lines up with what we found testing both on an active TypeScript project.

Why it's good: The quote sounds like a human. The follow-up connects it to the writer's
own experience. The reader gets two data points for the price of one.

Reference Page
The canonical reference for this skill is windsurf-vs-cursor-reddit.html.
When in doubt about a layout decision, styling choice, or wording pattern —
open that file. If the reference page does something a specific way, that is
the rule. Do not improvise structure. Do not add new section types.
New ideas go into the tone or content — not into the page architecture.

How to Invoke This Skill
User gives you one of these inputs:
Input A (explicit keyword):
"Build the page for: chatgpt vs claude for business emails"

Input B (pattern fill):
"X = Jasper AI, Y = Copy.ai, audience = marketing teams"

Input C (full keyword string):
"jasper vs copyai which is better 2026"
Your response sequence:

Confirm the two tools and the target keyword
Run the three required searches (do not skip)
Pull pricing, quotes, and one recent news item
Write the full HTML page following this skill
Output as a single complete HTML file

Do not ask for clarification before searching. Search first.
If you find something unexpected (tool was shut down, pricing changed dramatically,
one tool clearly dominates), surface that in the page — it becomes the unique angle.

Skill Maintenance Notes
Update this skill file when:

Site domain changes (update canonical URL formula)
Newsletter platform changes (update CTA fetch endpoint)
Color theme changes (update CSS token values in the "What Never Changes" section)
A new reference page is created that supersedes the windsurf example

Do not update this skill file to change content rules based on a single page's
performance. Wait for 10+ pages of data before changing tone or structure rules