#!/usr/bin/env python
from get_platform import get_platform
from config import make_urls
import os
import argparse

alias_to_browser = {
    'safa' : 'safari',
    'chro' : 'Google Chrome',
    'edge' : 'microsoft-edge',
}

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
        help="Search Type: video, general, ebook, zh")
    parser.add_argument("--browser", '-B', type=str, 
        help="Browser Type: safa, chro", default=default_browser)
    parser.add_argument("--debug", "-d", action="store_true")
    args = parser.parse_args()

    browser = alias_to_browser.get(args.browser, 'safa')
    keyword = input(
        f"Mode: {args.search_type}\n\
Browser: {browser}\n\
Please input keyword to search:\n")
    urls = make_urls(keyword, args.search_type, platform)
    search(urls, browser, platform, args.debug)

    # if args.search_type == 'video':
        # search(video_search_urls)
    # elif args.search_type == 'general':
        # search(general_search_urls)
    # elif args.search_type == 'ebook':
        # search(ebook_search_urls)
    # elif args.search_type == 'zh':
        # search(zh_search_urls)
    # else:
        # raise NotImplementedError

if __name__ == '__main__':
    main()