from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def check_path_exists(path: Path, description: str) -> None:
    assert path.exists(), f"Missing {description}: {path}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_write_a_blog_command() -> None:
    command_path = ROOT / ".claude" / "Commands" / "write-a-blog"
    check_path_exists(command_path, "write-a-blog command file")

    text = read_text(command_path)
    assert "Command name: write-a-blog" in text, "write-a-blog command file must declare the command name"
    assert "Use the BlogSkill instructions" in text, "Command file should reference BlogSkill instructions"


def check_blogskill_md() -> None:
    blog_skill = ROOT / "futuretech" / "blog" / "management" / "skills" / "BlogSkill.md"
    check_path_exists(blog_skill, "BlogSkill.md")

    text = read_text(blog_skill)
    assert "What This Skill Does" in text, "BlogSkill.md should contain the skill overview"
    assert "Page Architecture — Follow This Exactly" in text, "BlogSkill.md should include page architecture guidance"


def check_django_project() -> None:
    project_root = ROOT / "futuretech"
    manage_py = project_root / "manage.py"
    check_path_exists(project_root, "Django project folder")
    check_path_exists(manage_py, "manage.py")

    settings_py = project_root / "futuretech" / "settings.py"
    check_path_exists(settings_py, "Django settings.py")


def check_ai_tool_comparison_blog() -> None:
    blog_flow = ROOT / "futuretech" / "blog" / "management" / "skills" / "ai-tool-comparison-blog.md"
    check_path_exists(blog_flow, "ai-tool-comparison-blog.md")

    text = read_text(blog_flow)
    assert "Step 1 — Parse the Input" in text, "ai-tool-comparison-blog.md must include the command workflow steps"
    assert "Output Filename Pattern" in text, "ai-tool-comparison-blog.md must define output filename conventions"


def check_management_command_prompt() -> None:
    command_script = ROOT / "futuretech" / "blog" / "management" / "commands" / "write_a_blog.py"
    check_path_exists(command_script, "Django write_a_blog command")

    text = read_text(command_script)
    assert "ai-tool-comparison-blog.md" in text, "write_a_blog.py should reference ai-tool-comparison-blog.md"
    assert "Use the BlogSkill instructions from BlogSkill.md" in text, "write_a_blog.py should reference BlogSkill.md"


def run_dry_run_generation() -> None:
    print("Running dry-run generation test...")
    result = subprocess.run(
        [sys.executable, "./futuretech/manage.py", "write_a_blog", "gemini vs grok", "--dry-run"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, (
        f"Dry-run generation failed with exit code {result.returncode}. stderr:\n{result.stderr.strip()}"
    )

    output = result.stdout
    assert "<!DOCTYPE html>" in output, "Generated output must include HTML doctype"
    assert "<head>" in output and "<title>Gemini vs Grok" in output, "Generated HTML should include the expected title"
    assert "https://schema.org" in output, "Generated HTML should include schema JSON-LD"
    assert "class=\"reddit-quote\"" in output, "Generated HTML should include Reddit quote blocks"
    assert "class=\"compare-table-wrap\"" in output, "Generated HTML should include a head-to-head table wrapper"
    assert "class=\"price-card\"" in output, "Generated HTML should include pricing cards"
    assert "class=\"scenario-card\"" in output, "Generated HTML should include scenario cards"
    assert "class=\"cta-form\"" in output, "Generated HTML should include the third option CTA form"
    assert "FAQ" in output and "class=\"faq-section\"" in output, "Generated HTML should include the FAQ section"


def run_optional_django_check() -> None:
    try:
        result = subprocess.run(
            [sys.executable, "-m", "django", "--version"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        print("WARNING: Python executable not found; skipping Django version check.")
        return

    if result.returncode == 0:
        print(f"Django version: {result.stdout.strip()}")
    else:
        print("WARNING: Could not run 'python -m django --version'. Django may not be installed in this environment.")
        if result.stderr:
            print(result.stderr.strip())


def main() -> None:
    print("Running AI Claude Traffic test script...")
    check_write_a_blog_command()
    check_blogskill_md()
    check_ai_tool_comparison_blog()
    check_django_project()
    check_management_command_prompt()
    run_dry_run_generation()
    run_optional_django_check()
    print("\nPASS: AI Claude Traffic project tests all passed.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"FAIL: {exc}")
        sys.exit(1)
