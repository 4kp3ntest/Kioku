#!/usr/bin/env python

import requests
import urllib
from bs4 import BeautifulSoup
import sys


def crawl(pages, depth=None):
    indexed_url = [] # a list for the main and sub-HTML websites in the main website
    for i in range(depth):
        for page in pages:
            if page not in indexed_url:
                indexed_url.append(page)
                try:
                    c = requests.get(page)
                except:
                    print("Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.text)
                links = soup('a') #finding all the sub_links
                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urllib.parse.urljoin(page, link['href'])
                        if url.find("'") != -1:
                                continue
                        url = url.split('#')[0] 
                        if url[0:4] == 'http':
                                indexed_url.append(url)
        pages = indexed_url
    return indexed_url

def main():
    if len(sys.argv) == 2:
        site = sys.argv[1]
    else:
        site = ["https://wiki.archlinux.org/index.php/Pacman"]
    urls = crawl(site, depth=2)
    print(urls)


if __name__ == '__main__':
    main()

