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
    blog_skill = ROOT / "BlogSkill.md"
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
    check_django_project()
    run_optional_django_check()
    print("\nPASS: AI Claude Traffic command setup looks good.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"FAIL: {exc}")
        sys.exit(1)
