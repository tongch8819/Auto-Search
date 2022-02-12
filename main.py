#!/usr/bin/env python
from config import alias_to_name, make_urls
import os
import argparse

def augment_url(url):
    res = url.strip().replace(' ', '%20')
    return res

def search(urls, browser):
    for url in urls:
        url = augment_url(url)
        print("URL:", url)
        # macos dependent
        # os.system(f"open -a safari {url}")
        os.system(f"open -a '{browser}' {url}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_type", type=str, help="Search Type: video, general, ebook, zh")
    parser.add_argument("--browser", '-B', type=str, help="Browser Type: safa, chro", default='safa')
    # parser.add_argument("keyword", type=str, help="Search Keyword")
    # parser.add_argument("--lang", "-l", type=str, help="Keyword Language: zh, en", default="en")
    args = parser.parse_args()

    browser = alias_to_name.get(args.browser, 'safa')
    keyword = input(
        f"Mode: {args.search_type}\n\
Browser: {browser}\n\
Please input keyword to search:\n")
    urls = make_urls(keyword, args.search_type)
    search(urls, browser)
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