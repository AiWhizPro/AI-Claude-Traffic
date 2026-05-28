# AI Claude Traffic — Agent Guide

## What this repository is
- A small Django project under `futuretech/`.
- It includes a custom AI content workflow for generating publish-ready comparison pages.
- The main AI flow is defined by `futuretech/blog/management/skills/BlogSkill.md` and `futuretech/blog/management/skills/ai-tool-comparison-blog.md`.
- A custom Claude metadata command lives at `.claude/Commands/write-a-blog`.

## Key files to read first
- `README.md` — project overview and run instructions.
- `.claude/Commands/write-a-blog` — command metadata and expected generation behavior.
- `futuretech/blog/management/skills/BlogSkill.md` — page architecture, tone, and section rules.
- `futuretech/blog/management/skills/ai-tool-comparison-blog.md` — prompt workflow and generation template guidance.
- `futuretech/blog/management/commands/write_a_blog.py` — Django management command implementation.
- `claude_integration.py` — generator helper used by the command.
- `test_ai_claude_traffic.py` — sanity tests for the command and repository layout.

## How to help effectively
- Preserve the existing AI workflow and prompt structure.
- When changing generation logic, keep the `BlogSkill.md` and `ai-tool-comparison-blog.md` docs as the source of truth.
- Do not remove or restructure mandatory page sections described in `BlogSkill.md`.
- Follow the short sentence, active voice, honest verdict style already present in the docs.
- For Django work, add apps under `futuretech/`, register them in `futuretech/futuretech/settings.py`, and wire views/urls in `futuretech/futuretech/urls.py`.

## Recommended commands
- `& .\venv\Scripts\Activate.ps1`
- `python .\test_ai_claude_traffic.py`
- `cd futuretech && python manage.py migrate`
- `cd futuretech && python manage.py runserver`
- `cd futuretech && python manage.py write_a_blog "Cursor vs Copilot" --dry-run`

## Important conventions
- The custom command output should be full HTML with `<head>`, schema JSON-LD, hero, TOC, quick verdict, Reddit-style quotes, comparison table, pricing, scenarios, third-option CTA, FAQ, and footer.
- Always use the exact structure and section order spelled out in `BlogSkill.md`.
- Keep generated content concise, factual, and developer-friendly.
- Avoid marketing fluff, corporate speak, and generic unsupported claims.

## Notes for future customization
- This repo has no existing `.github/copilot-instructions.md` file yet.
- If additional agent guidance is needed, add a second customization file for the Django backend or the AI generation workflow.
- Maintain links to existing documentation instead of copying large blocks of text.
