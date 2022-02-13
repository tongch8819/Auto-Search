#!/usr/bin/env python
from get_platform import get_platform
from config import make_urls, alias_to_browser
import os
import argparse

def augment_url(url):
    res = url.strip().replace(' ', '%20')
    return res

def search(urls, browser, platform, debug=False):
    for url in urls:
        url = augment_url(url)

        if platform == 'Windows':
            url = url.replace('&', '^&')  # escape
            cmd = (f"start {browser}:{url}")
        else:
            # macos dependent
            cmd = (f"start {browser}:{url}")
        if debug:
            print(cmd)
        else:
            os.system(cmd)

def main():
    platform = get_platform()
    default_browser = 'edge' if platform == 'Windows' else 'safa'

    parser = argparse.ArgumentParser()
    parser.add_argument("search_type", type=str, 
        help="Search Type: video, general, ebook, zh, enw")
    parser.add_argument("--browser", '-B', type=str, 
        help="Browser Type: safa, chro", default=default_browser)
    parser.add_argument("--debug", "-d", action="store_true")
    args = parser.parse_args()

    browser = alias_to_browser.get(args.browser, default_browser)
    keyword = input(
        f"Mode: {args.search_type}\n\
Browser: {browser}\n\
Please input keyword to search:\n")
    urls = make_urls(keyword, args.search_type, platform)
    search(urls, browser, platform, args.debug)

if __name__ == '__main__':
    main()