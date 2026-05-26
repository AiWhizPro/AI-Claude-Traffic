import urllib.request
import urllib.error
from pathlib import Path
import sys

HOME_URL = 'http://127.0.0.1:8000/'


def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode('utf-8', errors='replace')
    except urllib.error.URLError as error:
        print(f'WARN: could not fetch {url}: {error}')
        return None


def load_template(path):
    try:
        return Path(path).read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'FAIL: Template file not found: {path}')
        sys.exit(1)


def assert_contains(source, fragment, message):
    if fragment not in source:
        print(f'FAIL: {message}')
        print(f'  Expected to find: {fragment}')
        sys.exit(1)
    print(f'OK: {message}')


def assert_not_contains(source, fragment, message):
    if fragment in source:
        print(f'FAIL: {message}')
        print(f'  Unexpected fragment found: {fragment}')
        sys.exit(1)
    print(f'OK: {message}')


def run_checks(home_html, header_html):
    assert_contains(home_html, 'Memphis Style Home', 'Page title block is set to Memphis Style Home')
    assert_contains(header_html, 'Memphis Studio', 'Header branding has Memphis Studio text')
    assert_contains(home_html, 'rounded-[2rem]', 'Hero section uses rounded corners')
    assert_contains(home_html, 'hero-grid', 'Hero section uses Memphis background grid styling')
    assert_contains(home_html, 'Designed for calm, modern content', 'Hero heading text matches Memphis style')
    assert_contains(home_html, 'text-memphis-900', 'Memphis dark text tone is present')
    assert_contains(home_html, 'bg-memphis-50', 'Memphis surface background uses memphis-50')

    assert_not_contains(home_html, '<form', 'Homepage has no analyzer input form')
    assert_not_contains(home_html, 'Analyze</button>', 'Homepage has no Analyze button')
    assert_not_contains(header_html, 'Analyze</a>', 'Header has no Analyze nav button')
    assert_not_contains(home_html + header_html, 'Web Page Analyzer', 'Homepage has no old analyzer branding text')

    assert_contains(header_html, 'class="text-memphis-700 hover:text-memphis-900">Home</a>', 'Header still includes Home navigation')


if __name__ == '__main__':
    print('Checking Memphis UI updates...')
    home_html = fetch(HOME_URL)
    header_html = None

    if home_html is None:
        print('Falling back to template source checks because the local server is not running.')
        base_dir = Path(__file__).resolve().parent
        home_path = base_dir / 'futuretech' / 'blog' / 'templates' / 'blog' / 'home.html'
        header_path = base_dir / 'futuretech' / 'blog' / 'templates' / 'blog' / 'includes' / 'header.html'
        home_html = load_template(home_path)
        header_html = load_template(header_path)
    else:
        print('Fetched homepage successfully from local server.')
        # Load header separately from the template source for header-specific assertions.
        base_dir = Path(__file__).resolve().parent
        header_path = base_dir / 'futuretech' / 'blog' / 'templates' / 'blog' / 'includes' / 'header.html'
        header_html = load_template(header_path)

    run_checks(home_html, header_html)
    print('UI Memphis tests passed')
    sys.exit(0)
