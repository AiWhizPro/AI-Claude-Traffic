from __future__ import annotations

import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECT_DIR = ROOT / "futuretech"
BASE_TEMPLATE = PROJECT_DIR / "blog" / "templates" / "blog" / "base.html"
MEMPHIS_CSS = PROJECT_DIR / "blog" / "static" / "blog" / "memphis" / "styles.css"
HOME_TEMPLATE = PROJECT_DIR / "blog" / "templates" / "blog" / "home.html"
SITEMAP_FILE = ROOT / "public" / "sitemap.xml"
HOME_URL = "http://127.0.0.1:8000/"


def fetch_url(url: str) -> str | None:
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, ConnectionRefusedError):
        return None


def test_project_structure_exists() -> None:
    assert PROJECT_DIR.exists(), f"Missing Django project folder: {PROJECT_DIR}"
    assert (PROJECT_DIR / "manage.py").exists(), "Missing manage.py"
    assert (PROJECT_DIR / "futuretech" / "settings.py").exists(), "Missing settings.py"
    assert BASE_TEMPLATE.exists(), "Missing base template"
    assert MEMPHIS_CSS.exists(), "Missing Memphis stylesheet"
    assert HOME_TEMPLATE.exists(), "Missing home template"
    assert SITEMAP_FILE.exists(), "Missing public/sitemap.xml"


def test_base_template_loads_memphis_css() -> None:
    text = BASE_TEMPLATE.read_text(encoding="utf-8")
    assert "{% load static %}" in text, "Base template must load Django static"
    assert "{% static 'blog/memphis/styles.css' %}" in text, "Base template must link Memphis stylesheet"


def test_memphis_css_contains_theme_rules() -> None:
    text = MEMPHIS_CSS.read_text(encoding="utf-8")
    assert ":root {" in text, "Memphis stylesheet must define root CSS variables"
    assert "body::before" in text, "Memphis stylesheet must include the polka-dot overlay"
    assert ".nav {" in text, "Memphis stylesheet must include navigation styling"


def test_sitemap_contains_absolute_url() -> None:
    text = SITEMAP_FILE.read_text(encoding="utf-8")
    assert "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">" in text, "Sitemap must use the correct XML namespace"
    assert "<loc>https://" in text, "Sitemap must contain at least one absolute https URL"


def test_live_server_serves_memphis_stylesheet() -> None:
    homepage = fetch_url(HOME_URL)
    if homepage is None:
        raise AssertionError("Local Django server is not running at http://127.0.0.1:8000/")

    assert "blog/memphis/styles.css" in homepage, "Homepage must include the Memphis stylesheet URL"
    css_url = HOME_URL.rstrip("/") + "/static/blog/memphis/styles.css"
    css_content = fetch_url(css_url)
    assert css_content is not None, "Memphis stylesheet must be served by the Django server"
    assert "/* Memphis / Playful Geometric Style */" in css_content, "Served stylesheet must be the Memphis CSS"
