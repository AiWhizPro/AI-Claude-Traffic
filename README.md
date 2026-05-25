# AI Claude Traffic

A small Django-based project scaffold with a custom `.claude` command definition for generating AI-powered blog content.

## What is included

- `futuretech/` — Django project skeleton
- `.claude/Commands/write-a-blog` — custom command metadata for the `write-a-blog` action
- `BlogSkill.md` — instructions for building publish-ready comparison articles
- `test_ai_claude_traffic.py` — basic project sanity check script
- `claude_integration.py` — starter Claude integration helper

## Notes on dependencies

This repository currently does not include a `requirements.txt` file. That is not strictly required to run the existing Django project because the project is already based on a Python virtual environment (`venv`).

If you want a reproducible install later, create one from the active environment:

```powershell
pip freeze > requirements.txt
```

## Run the project

Activate the virtual environment:

```powershell
& .\venv\Scripts\Activate.ps1
```

Run Django migrations:

```powershell
cd futuretech
python manage.py migrate
```

Run the development server:

```powershell
python manage.py runserver
```

Create a blog post directly from the command line without using a separate editor UI:

```powershell
cd "c:\Users\New User\Desktop\AI Claude Traffic"
.\write-a-blog.ps1 "Cursor vs ChatGPT"
```

This command generates a publish-ready HTML blog post and saves it as a published `BlogPost` that appears automatically on the homepage.

## Local generation

The file `claude_integration.py` now generates a publish-ready placeholder HTML page locally.

You do not need to set an API key or use an external Anthropic integration to run the `write-a-blog` command.

## Next steps

- Add a Django app under `futuretech/`
- Register the app in `futuretech/futuretech/settings.py`
- Add views, URLs, and templates for your AI workflow
- Expand `claude_integration.py` with real prompt handling and dataset logic
