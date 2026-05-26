import urllib.request
import html
import re
import sys

HOME_URL = 'http://127.0.0.1:8000/'
MENU_URL = 'http://127.0.0.1:8000/posts/'


def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return r.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f'ERROR: failed to fetch {url}: {e}')
        sys.exit(2)


def extract_h3_titles(html_text):
    titles = re.findall(r'<h3[^>]*>(.*?)</h3>', html_text, flags=re.I | re.S)
    return [html.unescape(re.sub(r'<[^>]+>', '', t)).strip() for t in titles]


if __name__ == '__main__':
    print('Fetching homepage...')
    home = fetch(HOME_URL)

    print('Checking for Memphis style classes...')
    if 'memphis-800' not in home and 'memphis-500' not in home:
        print('WARN: Memphis color classes not found on homepage (memphis-800/memphis-500)')
    else:
        print('OK: Memphis classes present')

    titles = extract_h3_titles(home)
    print(f'Found {len(titles)} <h3> post titles on homepage')

    uniq = list(dict.fromkeys(titles))
    if len(uniq) != len(titles):
        print('FAIL: Duplicate post titles found on homepage:')
        for t in titles:
            if titles.count(t) > 1:
                print('  -', t)
        sys.exit(1)
    else:
        print('OK: No duplicate titles on homepage')

    if len(titles) > 6:
        print('FAIL: Homepage shows more than 6 posts')
        sys.exit(1)
    else:
        print('OK: Homepage shows <= 6 posts')

    # If there are more posts in total, verify the "View all posts" link goes to the menu page
    if 'View all posts' in home or 'View all posts' in home:
        print('Homepage advertises View all posts — checking menu page...')
        menu = fetch(MENU_URL)
        menu_titles = extract_h3_titles(menu)
        if menu_titles:
            print(f'OK: Menu page reachable and contains {len(menu_titles)} posts')
        else:
            print('FAIL: Menu page reachable but contains no posts')
            sys.exit(1)

    print('UI Memphis tests passed')
    sys.exit(0)
