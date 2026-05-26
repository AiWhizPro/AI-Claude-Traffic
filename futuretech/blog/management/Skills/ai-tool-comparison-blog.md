AI Tool Comparison Blog — Skill Guide
What This Skill Does
Turns a single keyword like "cursor" or "cursor vs github copilot" into a
complete, publish-ready HTML comparison page following the exact branded template.
Output: One .html file saved to /mnt/user-data/outputs/ and presented
to the user via present_files.

Step-by-Step Workflow
Step 1 — Parse the Input
Extract Tool X and Tool Y from the keyword:
InputTool XTool Y"cursor"CursorGitHub Copilot (default main competitor)"cursor vs copilot"CursorGitHub Copilot"windsurf vs cursor"WindsurfCursor"v0 vs bolt"v0Bolt
If Tool Y is not provided, infer the most-discussed competitor from the pattern
"[X] vs [main-rival] reddit" — the top Reddit result will confirm it.
Extract the Year from the keyword or default to the current year.

Step 2 — Run Web Searches (Required Before Writing)
Run all five searches. Do not skip any. Collect real numbers, prices, and
community opinions. Use the results to fill every {{PLACEHOLDER}} in the template.
Search 1: "[X] vs [Y] reddit [Year]"
Search 2: "[X] pricing [Year]"
Search 3: "[Y] pricing [Year]"
Search 4: "[X] vs [Y] benchmark OR review [Year]"
Search 5: "[X] recent news OR updates [Year]"
Extract and note down:

Current price tiers for X and Y (free / pro / team)
Any recent bugs, controversies, or major feature launches (last 6 months)
Real benchmark numbers if available (accuracy %, speed, task counts)
2–3 authentic community opinions (Reddit, HN, GitHub Discussions)
Unique strengths and weaknesses for X and Y


Step 3 — Fill the Template
Read references/html-template.html for the full page structure.
Replace every {{PLACEHOLDER}} with researched content.
Key placeholders and how to fill them:
PlaceholderSource{{TOOL_X}}Tool name, e.g. "Cursor"{{TOOL_Y}}Tool name, e.g. "GitHub Copilot"{{YEAR}}Current year{{SLUG}}kebab-case filename, e.g. cursor-vs-github-copilot{{META_DESCRIPTION}}150-char summary for SEO{{HERO_SUBTITLE}}1-sentence hook. Honest. No hype.{{VERDICT_X_BADGE}}e.g. "🚀 More Powerful"{{VERDICT_X_BODY}}3–5 sentences. Best case for X. Honest weaknesses.{{VERDICT_Y_BADGE}}e.g. "🛡 More Practical"{{VERDICT_Y_BODY}}3–5 sentences. Best case for Y. Honest weaknesses.{{REDDIT_QUOTE_1}} through {{REDDIT_QUOTE_3}}Real paraphrased community takes{{TABLE_ROWS}}8–10 comparison rows (see table format in template){{PRICE_X_MONTHLY}}Verified current price{{PRICE_Y_MONTHLY}}Verified current price{{PRICE_X_FEATURES}}5–6 <li> items{{PRICE_Y_FEATURES}}5–6 <li> items{{SCENARIO_CARDS}}6 scenario cards (3 per tool) — see format in template{{THIRD_OPTION_BODY}}3 paragraphs: landscape volatility → two-tool stack → CTA lead-in{{FAQ_ITEMS}}5–6 FAQ blocks (see format in template){{AUTHOR}}Harsha Vardhan{{DATE}}Today's date

Step 4 — Apply the House Tone (Non-Negotiable)
Read references/tone-guide.md before writing any body copy.
Quick checklist before saving:

 Every sentence under 20 words? (aim for 12–15)
 No "leverages", "harnesses", "game-changing", "revolutionary"?
 Copilot wins on at least 3 criteria (honest, not shill for X)?
 At least one negative about Tool X mentioned in the verdict?
 Numbers cited (prices, benchmarks, dates) all verified from searches?
 Highlights used naturally — not every sentence has a coloured span?


Step 5 — Save and Present
Save the filled HTML to /mnt/user-data/outputs/{{SLUG}}-reddit.html.
Call present_files with the output path.
Do not dump the raw HTML into the chat. Just present the file and give a
3-sentence summary of the key verdict (Tool X wins for X scenario, Tool Y wins
for Y scenario).

Reference Files
FileWhen to Readreferences/html-template.htmlStep 3 — template with all placeholdersreferences/tone-guide.mdStep 4 — tone rules and banned words

Examples of Good Output
Good — Verdict Card Body (Cursor)

The better AI coding experience for heavy work. 30% faster per task.
Composer edits 10–50 files in one go — Copilot can't match this. The catch:
$20/month, VS Code only, and a March 2026 bug briefly reverted committed code.
Best for solo developers who live in VS Code.

Bad — Verdict Card Body (Cursor)

Cursor leverages cutting-edge AI to revolutionise your development workflow,
offering an unparalleled coding experience that harnesses the power of
large language models.


Good — Scenario Card

You inherited a codebase you didn't write.
Cursor's semantic indexing lets you query the entire repo in plain English.
New team members come up to speed in seconds, not hours.

Bad — Scenario Card

Cursor provides comprehensive codebase understanding capabilities that enable
developers to efficiently navigate and comprehend complex software architectures.


Good — Reddit Quote Context

The most upvoted take on r/programming isn't about features.
It's about a different question entirely — one that explains why this debate
has no universal answer.

Bad — Reddit Quote Context

The Reddit community has expressed diverse and multifaceted opinions
regarding the relative merits of these two innovative tools.


Output Filename Pattern
{tool-x-slug}-vs-{tool-y-slug}-reddit.html
Examples:

cursor-vs-github-copilot-reddit.html
windsurf-vs-cursor-reddit.html
v0-vs-bolt-reddit.html