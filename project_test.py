from __future__ import annotations

import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT_DIR = ROOT / "futuretech"
BASE_TEMPLATE = PROJECT_DIR / "blog" / "templates" / "blog" / "base.html"
MEMPHIS_CSS = PROJECT_DIR / "blog" / "static" / "blog" / "memphis" / "styles.css"
HOME_TEMPLATE = PROJECT_DIR / "blog" / "templates" / "blog" / "home.html"
SITEMAP_FILE = ROOT / "public" / "sitemap.xml"
HOME_URL = "http://127.0.0.1:8000/"


def assert_exists(path: Path, description: str) -> None:
    if not path.exists():
        raise AssertionError(f"Missing {description}: {path}")
    print(f"OK: Found {description}")


def assert_contains(source: str, substring: str, description: str) -> None:
    if substring not in source:
        raise AssertionError(f"Missing {description}: expected to find '{substring}'")
    print(f"OK: {description}")


def fetch_url(url: str) -> str | None:
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, ConnectionRefusedError) as exc:
        print(f"WARN: Could not fetch {url}: {exc}")
        return None


def run_file_checks() -> None:
    print("Running file checks...")
    assert_exists(PROJECT_DIR, "Django project folder")
    assert_exists(PROJECT_DIR / "manage.py", "Django manage.py")
    assert_exists(PROJECT_DIR / "futuretech" / "settings.py", "Django settings.py")
    assert_exists(BASE_TEMPLATE, "base template")
    assert_exists(MEMPHIS_CSS, "Memphis stylesheet")
    assert_exists(HOME_TEMPLATE, "home template")
    assert_exists(SITEMAP_FILE, "sitemap.xml in public root")

    base_text = BASE_TEMPLATE.read_text(encoding="utf-8")
    assert_contains(base_text, "{% load static %}", "Django static template tag is loaded")
    assert_contains(base_text, "{% static 'blog/memphis/styles.css' %}", "Memphis stylesheet is linked in base template")

    css_text = MEMPHIS_CSS.read_text(encoding="utf-8")
    assert_contains(css_text, ":root {", "Memphis CSS root variables exist")
    assert_contains(css_text, "body::before", "Memphis CSS includes the polka-dot overlay")
    assert_contains(css_text, ".nav {", "Memphis CSS contains navigation styling")

    sitemap_text = SITEMAP_FILE.read_text(encoding="utf-8")
    assert_contains(sitemap_text, "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">", "Sitemap file has a valid urlset root")
    assert_contains(sitemap_text, "<loc>https://", "Sitemap contains at least one absolute https URL")
    print("File checks passed.\n")


def run_live_checks() -> None:
    print("Running live server checks...")
    homepage = fetch_url(HOME_URL)
    if homepage is None:
        print("Skipped live homepage checks because the server is not running.")
        return

    assert_contains(homepage, "href=\"/static/blog/memphis/styles.css\"", "Homepage includes Memphis stylesheet URL")
    css_url = HOME_URL.rstrip("/") + "/static/blog/memphis/styles.css"
    css_content = fetch_url(css_url)
    if css_content is None:
        raise AssertionError("Could not load Memphis stylesheet from the running server")
    assert_contains(css_content, "/* Memphis / Playful Geometric Style */", "Memphis stylesheet is served by the server")
    print("Live server checks passed.\n")


def main() -> int:
    try:
        run_file_checks()
        run_live_checks()
    except AssertionError as exc:
        print(f"FAIL: {exc}")
        return 1
    print("PASS: Project test script completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
