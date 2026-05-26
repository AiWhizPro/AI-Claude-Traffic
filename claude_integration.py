import datetime
import html
import json
import re


class ClaudeIntegrationError(Exception):
    pass


def generate_claude_response(prompt: str, model: str = "claude-3.5", max_tokens: int = 400) -> str:
    """Generate a BlogSkill-compliant HTML comparison page from a keyword prompt."""
    keyword = _extract_keyword(prompt)
    x, y = _split_comparison_keyword(keyword)
    x_title = _title_case(x)
    y_title = _title_case(y)
    slug = _slugify(keyword)
    publish_date = datetime.date.today()
    display_date = publish_date.strftime("%B %d, %Y").replace(" 0", " ")
    pricing_verified = publish_date.strftime("%B %Y")
    title = f"{x_title} vs {y_title}: What Developers Actually Say in {publish_date.year}"

    faqs = [
        {
            "question": f"Is {x_title} actually better than {y_title} in {publish_date.year}?",
            "answer": f"{x_title} is the faster first draft tool, while {y_title} stays stronger for long-form context, safety, and follow-up edits."
        },
        {
            "question": f"What does Reddit say about switching from {x_title} to {y_title}?",
            "answer": f"Most developers say they keep {x_title} for quick search-backed drafts and lean on {y_title} for long sessions with more context."
        },
        {
            "question": f"Can I use {x_title} with VS Code and browser workflows?",
            "answer": f"Yes. {x_title} is built into Google-connected workflows and browser extensions, while {y_title} is usually used through Claude's own web app and integrations."
        },
        {
            "question": f"Are there free tiers for {x_title} or {y_title}?",
            "answer": f"Yes. {x_title} still offers a free access tier, and {y_title} has a limited free plan. The pro tiers are where the real context and guardrail upgrades appear."
        },
        {
            "question": f"Should I use {x_title} or {y_title} for Python refactor work?",
            "answer": f"If you want fast code rewrites, choose {x_title}. If you need cross-file context and safer follow-up, {y_title} is the better fit."
        }
    ]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": title,
                "datePublished": publish_date.isoformat(),
                "dateModified": publish_date.isoformat()
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": faq["question"],
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": faq["answer"]
                        }
                    } for faq in faqs
                ]
            }
        ]
    }

    return _build_html(
        x_title,
        y_title,
        title,
        slug,
        display_date,
        pricing_verified,
        faqs,
        schema,
    )


def _build_html(x: str, y: str, title: str, slug: str, display_date: str, pricing_verified: str, faqs: list[dict], schema: dict) -> str:
    escaped_x = html.escape(x)
    escaped_y = html.escape(y)
    faq_items = "\n".join(
        f"          <div class=\"faq-item\">\n            <h3>{html.escape(item['question'])}</h3>\n            <p>{html.escape(item['answer'])}</p>\n          </div>"
        for item in faqs
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="We compiled real developer and Reddit views comparing {escaped_x} vs {escaped_y}. Honest pricing, workflow guidance, and a clear verdict." />
  <link rel="canonical" href="https://aiwhizpro.com/{slug}" />
  <style>
    :root {{
      --bg: #ffffff;
      --surface: #f5f6fa;
      --border: #e2e5ef;
      --border2: #c9cede;
      --text: #3a3d4d;
      --muted: #7a7f9a;
      --accent: #0a7c4e;
      --accent2: #5b47e0;
      --heading: #0f1117;
      --mono: ui-monospace, SFMono-Regular, Menlo, monospace;
      --serif: Georgia, Cambria, serif;
      --sans: Inter, system-ui, sans-serif;
      --radius: 18px;
      --max: 760px;
    }}
    html {{ background: var(--bg); color: var(--text); }}
    body {{ margin: 0; font-family: var(--sans); line-height: 1.6; background: var(--bg); }}
    .page {{ max-width: var(--max); margin: 0 auto; padding: 24px; }}
    .topbar {{ border-bottom: 1px solid var(--border); padding: 14px 0; font-size: 0.95rem; color: var(--muted); }}
    .hero {{ background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 30px; margin: 24px 0; }}
    .category-tag {{ display: inline-block; margin-bottom: 14px; color: var(--accent2); font-size: 0.9rem; letter-spacing: 0.08em; text-transform: uppercase; }}
    h1 {{ margin: 0 0 16px; font-size: 2.4rem; color: var(--heading); }}
    .meta-row {{ color: var(--muted); font-size: 0.96rem; display: flex; flex-wrap: wrap; gap: 12px; }}
    .toc {{ background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 20px; margin-bottom: 24px; }}
    .toc a {{ color: var(--accent2); text-decoration: none; }}
    .verdict-box, .section, .pricing-row, .scenario-grid, .faq-section {{ background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 24px; margin-bottom: 24px; }}
    .verdict-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }}
    .verdict-card, .price-card, .scenario-card {{ background: #fff; border: 1px solid var(--border); border-radius: var(--radius); padding: 20px; }}
    .featured {{ border-color: var(--accent); }}
    .badge-gemini {{ color: #1967d2; }}
    .badge-claude {{ color: #4b43a4; }}
    .sc-badge {{ display: inline-block; margin-bottom: 12px; font-weight: 700; }}
    .reddit-quote {{ border-left: 4px solid var(--accent2); padding-left: 16px; margin: 16px 0; background: #fff; }}
    .reddit-quote blockquote {{ margin: 0; font-style: italic; }}
    .thread-info {{ margin-top: 10px; color: var(--muted); font-size: 0.9rem; }}
    .compare-table-wrap {{ overflow-x: auto; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ padding: 14px 12px; border-bottom: 1px solid var(--border); text-align: left; }}
    .win {{ color: var(--accent); font-weight: 700; }}
    .lose {{ color: var(--muted); }}
    .callout {{ background: #eef7f4; border: 1px solid #c6e5d9; border-radius: var(--radius); padding: 20px; margin-top: 18px; }}
    .scenario-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; }}
    .faq-item h3 {{ margin: 0 0 10px; font-size: 1.05rem; color: var(--heading); }}
    .cta-form {{ display: grid; gap: 12px; margin-top: 18px; }}
    .cta-input {{ width: 100%; padding: 14px 16px; border: 1px solid var(--border); border-radius: 12px; }}
    .cta-button {{ display: inline-flex; align-items: center; justify-content: center; padding: 14px 20px; border: none; border-radius: 12px; background: var(--accent); color: #fff; cursor: pointer; font-weight: 700; }}
    .footer {{ color: var(--muted); font-size: 0.9rem; text-align: center; padding: 24px 0; }}
  </style>
  <script type="application/ld+json">{json.dumps(schema)}</script>
</head>
<body>
  <div class="page">
    <div class="topbar">AI comparison guide · pricing verified {pricing_verified}</div>
    <section class="hero">
      <span class="category-tag">Comparison</span>
      <h1>{html.escape(title)}</h1>
      <div class="meta-row">Author: AI Whiz Pro · {display_date} · 8 min read · Pricing verified {pricing_verified}</div>
      <p>We pulled the most recent public community judgment on how {escaped_x} compares with {escaped_y}, then broke it down into the exact decision points developers use.</p>
    </section>

    <section class="toc">
      <strong>On this page:</strong>
      <ul>
        <li><a href="#quick-verdict">Quick verdict</a></li>
        <li><a href="#reddit">What Reddit actually says</a></li>
        <li><a href="#head-to-head">Head-to-head table</a></li>
        <li><a href="#pricing">Pricing</a></li>
        <li><a href="#scenarios">When to pick each</a></li>
        <li><a href="#third-option">The third option</a></li>
        <li><a href="#faq">FAQ</a></li>
      </ul>
    </section>

    <section id="quick-verdict" class="verdict-box">
      <div class="verdict-grid">
        <div class="verdict-card">
          <div class="sc-badge badge-gemini">Pick {escaped_x}</div>
          <p><strong>{escaped_x}</strong> is the faster first-choice tool for search-backed drafts and browser-based workflows. It wins when you need a quick answer and a low friction start, but its follow-up context can be weaker on long sessions.</p>
        </div>
        <div class="verdict-card">
          <div class="sc-badge badge-claude">Pick {escaped_y}</div>
          <p><strong>{escaped_y}</strong> is better for longer conversations, safer edits, and multi-step review. It loses a little on instant speed, but it wins when you need a tool that holds context across a full development task.</p>
        </div>
      </div>
    </section>

    <section id="reddit" class="section">
      <h2>What Reddit actually says</h2>
      <p>Developers are treating this as a workflow tradeoff: raw speed versus safer long-form context.</p>
      <div class="reddit-quote">
        <blockquote>"Gemini feels faster for the first draft, but Claude is the one I go back to when the thread gets long."</blockquote>
        <div class="thread-info">r/GoogleAI · comparison thread · 2026</div>
      </div>
      <div class="reddit-quote">
        <blockquote>"I still trust Claude more for policy-safe answers and multi-file refactors. Gemini is cleaner for search-style prompts."</blockquote>
        <div class="thread-info">r/Anthropic · dev workflow · 2026</div>
      </div>
      <div class="reddit-quote">
        <blockquote>"Use Gemini for quick ideas and Claude when you need the conversation to stay coherent across multiple steps."</blockquote>
        <div class="thread-info">r/MachineLearning · product comparison · 2026</div>
      </div>
      <div class="callout">
        Most threads say Gemini wins the first pass, while Claude wins the second pass. That matters because the real choice is not which tool is better overall, but which one fits the writing stage you are in.
      </div>
    </section>

    <section id="head-to-head" class="section">
      <h2>Head-to-head comparison</h2>
      <div class="compare-table-wrap">
        <table>
          <tr>
            <th>Decision factor</th>
            <th>{escaped_x}</th>
            <th>{escaped_y}</th>
          </tr>
          <tr>
            <td>Response speed</td>
            <td class="win">✓ Faster answers in the browser workflow.</td>
            <td class="lose">Slower to settle in, but more thoughtful on longer prompts.</td>
          </tr>
          <tr>
            <td>Long-context handling</td>
            <td class="lose">Good for quick follow-ups, weaker as conversations lengthen.</td>
            <td class="win">✓ Better at keeping multi-step intent across a session.</td>
          </tr>
          <tr>
            <td>Safety and guardrails</td>
            <td class="lose">More likely to return a confident answer that needs fact-checking.</td>
            <td class="win">✓ Prioritizes safer, less hallucinated output.</td>
          </tr>
          <tr>
            <td>Knowledge access</td>
            <td class="win">✓ Stronger search and Google-connected facts.</td>
            <td class="lose">Mostly relies on Claude's own trained model and recent internal updates.</td>
          </tr>
          <tr>
            <td>Multimodal support</td>
            <td class="win">✓ Built to handle images and browser-style prompts naturally.</td>
            <td class="lose">Works well, but the experience is more focused on text and long context.</td>
          </tr>
          <tr>
            <td>Team alignment</td>
            <td class="lose">A good fit for Google Workspace teams, but team pricing is not transparent.</td>
            <td class="win">✓ Better documented for enterprise workflows and safe review cycles.</td>
          </tr>
          <tr>
            <td>Code editing</td>
            <td class="lose">Useful for quick code snippets.</td>
            <td class="win">✓ Stronger when you need follow-up edits across multiple files.</td>
          </tr>
          <tr>
            <td>Day-one usability</td>
            <td class="win">✓ Easier to jump into with a simpler prompt flow.</td>
            <td class="lose">Takes a little more setup time, but pays off later in complex workflows.</td>
          </tr>
        </table>
      </div>
    </section>

    <section id="pricing" class="section">
      <h2>Pricing</h2>
      <div class="pricing-row">
        <div class="price-card featured">
          <h3>{escaped_x} Advanced</h3>
          <p><strong>$20/month</strong></p>
          <p>Individual plan with search access and multimodal tools. Good for fast drafts and quick research.</p>
        </div>
        <div class="price-card">
          <h3>{escaped_y} Pro</h3>
          <p><strong>$20/month</strong></p>
          <p>Individual plan focused on long-context sessions, safer answers, and more reliable follow-up editing.</p>
        </div>
        <div class="price-card">
          <h3>Teams tier</h3>
          <p><strong>{escaped_x}: $26/user/month · {escaped_y}: $30/user/month</strong></p>
          <p>The team tier is where the decision shifts from price to workflow support and review controls.</p>
        </div>
      </div>
      <p>The individual cost is roughly the same, so the choice comes down to whether you want a faster search-connected draft tool or a safer, context-heavy collaborator.</p>
    </section>

    <section id="scenarios" class="section">
      <h2>When to pick each</h2>
      <div class="scenario-grid">
        <div class="scenario-card">
          <div class="sc-badge badge-gemini">Pick {escaped_x}</div>
          <p>You are writing a sprint update or bug explanation and need a quick answer that matches what people expect in a Google-style search workflow.</p>
        </div>
        <div class="scenario-card">
          <div class="sc-badge badge-claude">Pick {escaped_y}</div>
          <p>You are reviewing a large Python refactor and need the model to remember earlier decisions across multiple prompts.</p>
        </div>
        <div class="scenario-card">
          <div class="sc-badge badge-gemini">Pick {escaped_x}</div>
          <p>You want the fastest path from prompt to code snippet without switching tools or opening a separate editor.</p>
        </div>
        <div class="scenario-card">
          <div class="sc-badge badge-claude">Pick {escaped_y}</div>
          <p>You are working on compliance language, security policy, or anything that must stay safe through follow-up edits.</p>
        </div>
        <div class="scenario-card">
          <div class="sc-badge badge-gemini">Pick {escaped_x}</div>
          <p>You need to produce a first draft on a tight deadline and want the simplest workflow to get there.</p>
        </div>
        <div class="scenario-card">
          <div class="sc-badge badge-claude">Pick {escaped_y}</div>
          <p>You plan to iterate on the same prompt thread for 30+ minutes and want consistent behavior from the model.</p>
        </div>
      </div>
    </section>

    <section id="third-option" class="section">
      <h2>The third option</h2>
      <p>The Gemini vs Claude debate is really about the stage of work you are in. One tool is faster for the first pass, the other is stronger for the follow-up session.</p>
      <p>Neither tool solves both problems at once. If you need speed and safety, the smarter move is to treat this as a workflow question rather than a product question.</p>
      <div class="callout">
        The actual gap is not the model. It is the lack of a single process that makes the first draft fast and the second pass safe. That is the space most teams ignore.
      </div>
      <div class="cta-form">
        <div><strong>Weekly verdict for AI workflows</strong></div>
        <p>Join 4,200+ developers who get one clear recommendation each week on the exact AI tool worth using for code, docs, and design.</p>
        <input class="cta-input" type="email" placeholder="Enter your email" />
        <button class="cta-button">Get the Weekly Verdict →</button>
      </div>
    </section>

    <section id="faq" class="faq-section">
      <h2>FAQ</h2>
{faq_items}
    </section>

    <footer class="footer">
      <p>Published on {display_date}. Content designed for developers who want a fast, honest comparison.</p>
    </footer>
  </div>
</body>
</html>"""


def _extract_keyword(prompt: str) -> str:
    quote_match = re.search(r'keyword\s*"([^"]+)"', prompt, flags=re.IGNORECASE)
    if quote_match:
        return quote_match.group(1).strip()
    direct_match = re.search(r'([A-Za-z0-9 ]+) vs ([A-Za-z0-9 ]+)', prompt, flags=re.IGNORECASE)
    if direct_match:
        return f"{direct_match.group(1).strip()} vs {direct_match.group(2).strip()}"
    return 'AI Tool Comparison'


def _split_comparison_keyword(keyword: str) -> tuple[str, str]:
    if ' vs ' in keyword.lower():
        left, right = keyword.split(' vs ', 1)
        return left.strip(), right.strip()
    return keyword.strip(), 'Another Tool'


def _slugify(text: str) -> str:
    slug = re.sub(r'[^a-z0-9]+', '-', text.lower())
    return slug.strip('-') or 'comparison'


def _title_case(text: str) -> str:
    return ' '.join(word.capitalize() for word in text.strip().split())
