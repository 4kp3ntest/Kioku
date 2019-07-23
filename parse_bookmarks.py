#!/usr/bin/python3

import sys
import re

"""
The idea is to parse my bookmarks by the provided tags to better group and structurize them together

reads a bookmark.html file as cmd arg
"""

def main():
    try:
        with open(sys.argv[1]) as fp:
            raw = fp.read()
    except:
        print('[!] Could not open file "{}"'.format(sys.argv[1]))
        exit()

    raw_lines = raw.split('\n')[:-1]
    ret = []
    tag_d = {}
    for i in raw_lines:
        # Get URL and tags [[URL, tags],..]
        tmp = re.search('<A HREF="(.*?)".*?">(.*?)</A>', i)
        if tmp:
            ret.append(tmp.groups())

    # 
    for i in ret:
        addr = i[0]
        name = i[1]
        tags = name.split(' ')
        if tags[0] not in tag_d:
            tag_d[tags[0]] = 1 
        else:
            tag_d[tags[0]] += 1
    for i in tag_d:
        print(i)

    print(len(ret))
        

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('[*] Usage: {} bookmark.html'.format(__file__))
    else:
        main()

