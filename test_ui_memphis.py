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


def run_checks(base_html, home_html, header_html, footer_html):
    # Typography
    assert_contains(base_html, "'Poppins'", 'Poppins font is included in the project base styles')
    assert_contains(base_html, 'font-family: \'Poppins\', sans-serif', 'Poppins is set as the body font')

    # Memphis palette
    assert_contains(base_html, '--color-primary: #e8879f;', 'Primary color variable is defined')
    assert_contains(base_html, '--color-secondary: #4db8a8;', 'Secondary color variable is defined')
    assert_contains(base_html, '--color-accent: #f5d76e;', 'Accent color variable is defined')
    assert_contains(base_html, '--color-background: #faf8f5;', 'Background color variable is defined')
    assert_contains(base_html, '--color-surface: #fffef7;', 'Surface color variable is defined')
    assert_contains(base_html, '--color-text: #1a1a2e;', 'Text color variable is defined')

    # Design properties
    assert_contains(base_html, '--radius: 12px;', 'Border radius is set to 12px')
    assert_contains(base_html, '--border-width: 3px;', 'Border width is set to 3px')
    assert_contains(base_html, '--shadow-offset: 4px 4px;', 'Shadow offset is set to 4px 4px')
    assert_contains(base_html, 'box-shadow: var(--shadow-offset) var(--shadow-offset)', 'Offset shadows use the configured shadow offset')
    assert_contains(base_html, 'border-radius: var(--radius)', 'Surface card border radius is applied')

    # Surface card styling
    assert_contains(base_html, '.surface-card', 'Surface card helper class is defined')
    assert_contains(base_html, 'background: var(--color-surface)', 'Surface cards use the surface background color')
    assert_contains(base_html, 'border: var(--border-width) solid', 'Bold borders are defined for surface cards')
    assert_contains(base_html, 'box-shadow: var(--shadow-offset) var(--shadow-offset) 0', 'Surface cards use offset shadows')

    # Header and footer styling
    assert_contains(header_html, 'surface-card', 'Header uses the surface card style')
    assert_contains(header_html, 'bg-memphis-100', 'Header uses the Memphis surface tone')
    assert_contains(footer_html, 'bg-memphis-100', 'Footer uses the Memphis surface tone')

    # Page-specific checks
    assert_contains(home_html, 'text-memphis-800', 'Homepage uses Memphis text color styling')
    assert_contains(home_html, 'bg-memphis-50', 'Homepage uses Memphis background styling')

    assert_not_contains(base_html, 'font-family: -apple-system', 'Base styles do not use default system font stacks')


if __name__ == '__main__':
    print('Checking Memphis UI updates...')
    home_html = fetch(HOME_URL)
    base_dir = Path(__file__).resolve().parent
    base_path = base_dir / 'futuretech' / 'blog' / 'templates' / 'blog' / 'base.html'
    home_path = base_dir / 'futuretech' / 'blog' / 'templates' / 'blog' / 'home.html'
    header_path = base_dir / 'futuretech' / 'blog' / 'templates' / 'blog' / 'includes' / 'header.html'
    footer_path = base_dir / 'futuretech' / 'blog' / 'templates' / 'blog' / 'includes' / 'footer.html'

    base_html = load_template(base_path)
    header_html = load_template(header_path)
    footer_html = load_template(footer_path)

    if home_html is None:
        print('Falling back to template source checks because the local server is not running.')
        home_html = load_template(home_path)
    else:
        print('Fetched homepage successfully from local server.')

    run_checks(base_html, home_html, header_html, footer_html)
    print('UI Memphis tests passed')
    sys.exit(0)
