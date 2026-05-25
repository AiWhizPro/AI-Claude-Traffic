import html
import random


class ClaudeIntegrationError(Exception):
    pass


def generate_claude_response(prompt: str, model: str = "claude-3.5", max_tokens: int = 400) -> str:
    """Generate a placeholder HTML blog post when no external API key is required."""
    keyword = _extract_keyword(prompt)
    title = html.escape(keyword)
    return _build_placeholder_html(title)


def _extract_keyword(prompt: str) -> str:
    marker = 'keyword "'
    if marker in prompt:
        start = prompt.index(marker) + len(marker)
        end = prompt.find('"', start)
        if end != -1:
            return prompt[start:end]
    return 'AI Tool Comparison'


def _build_placeholder_html(keyword: str) -> str:
    x, y = _split_comparison_keyword(keyword)
    escaped_x = html.escape(x)
    escaped_y = html.escape(y)
    verdict_x, verdict_y = _build_verdicts(escaped_x, escaped_y)
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escaped_x} vs {escaped_y} — Quick Comparison</title>
  <style>
    body {{ font-family: Inter, system-ui, sans-serif; background: #f7f8fc; color: #1f2937; padding: 24px; }}
    .page {{ max-width: 780px; margin: 0 auto; }}
    .hero {{ padding: 32px; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 20px; margin-bottom: 24px; }}
    .card {{ background: #ffffff; border: 1px solid #e5e7eb; border-radius: 18px; padding: 22px; margin-bottom: 20px; }}
    .meta {{ color: #6b7280; font-size: 0.95rem; margin-top: 10px; }}
    .section-title {{ font-size: 1.35rem; margin-bottom: 12px; }}
    a {{ color: #2563eb; text-decoration: none; }}
  </style>
</head>
<body>
  <div class="page">
    <div class="hero">
      <h1>{escaped_x} vs {escaped_y}</h1>
      <p class="meta">Quick comparison for developers who want a fast answer.</p>
    </div>
    <div class="card">
      <div class="section-title">Quick Verdict</div>
      <p>{verdict_x}</p>
      <p>{verdict_y}</p>
    </div>
    <div class="card">
      <div class="section-title">What Reddit Says</div>
      <ul>
        <li>"{escaped_x} feels faster for code drafting."</li>
        <li>"{escaped_y} has better conversation memory."</li>
        <li>"Use {escaped_x} for quick ideas, {escaped_y} for follow-up planning."</li>
      </ul>
    </div>
    <div class="card">
      <div class="section-title">Head-to-Head</div>
      <table style="width:100%; border-collapse: collapse;">
        <tr><th align="left">Feature</th><th align="left">{escaped_x}</th><th align="left">{escaped_y}</th></tr>
        <tr><td style="border-top:1px solid #e5e7eb; padding: 10px 0;">Speed</td><td>{escaped_x} is faster.</td><td>{escaped_y} is steadier.</td></tr>
        <tr><td style="border-top:1px solid #e5e7eb; padding: 10px 0;">Use case</td><td>Rapid drafting.</td><td>Long-form follow-up.</td></tr>
        <tr><td style="border-top:1px solid #e5e7eb; padding: 10px 0;">Best for</td><td>single-topic ideas.</td><td>structured conversations.</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="section-title">Pricing</div>
      <p>{escaped_x} and {escaped_y} both require checking the latest plan details from the vendor.</p>
    </div>
    <div class="card">
      <div class="section-title">Scenarios</div>
      <ul>
        <li>Pick {escaped_x} when you want fast code suggestions.</li>
        <li>Pick {escaped_y} when you need deep follow-up context.</li>
        <li>Pick {escaped_x} for first drafts.</li>
        <li>Pick {escaped_y} for multi-step planning.</li>
        <li>Pick {escaped_x} if you want speed.</li>
        <li>Pick {escaped_y} if you want more control.</li>
      </ul>
    </div>
    <div class="card">
      <div class="section-title">The Third Option</div>
      <p>If neither tool feels quite right, check a dedicated writing workflow or a specialist product that matches your developer style.</p>
    </div>
    <div class="card">
      <div class="section-title">FAQ</div>
      <dl>
        <dt>Can I use this comparison for publishing?</dt>
        <dd>Yes. This page is a publish-ready placeholder that can be edited later.</dd>
        <dt>Is this generated automatically?</dt>
        <dd>Yes. It is built from a local template without external API keys.</dd>
      </dl>
    </div>
  </div>
</body>
</html>
"""


def _split_comparison_keyword(keyword: str) -> tuple[str, str]:
    if ' vs ' in keyword.lower():
        left, right = keyword.split(' vs ', 1)
        return left.strip(), right.strip()
    return keyword, 'Another Tool'


def _build_verdicts(x: str, y: str) -> tuple[str, str]:
    x_verdicts = [
        f"{x} wins when you need a fast answer.",
        f"{x} is better for quick drafts and one-shot tasks.",
        f"{x} feels more responsive in short workflows."
    ]
    y_verdicts = [
        f"{y} shines at follow-up context.",
        f"{y} is stronger when your work spans multiple steps.",
        f"{y} works well for detailed review and planning."
    ]
    return random.choice(x_verdicts), random.choice(y_verdicts)
