#!/usr/bin/python3

import sys
import re


def main():
    try:
        with open(sys.argv[1]) as fp:
            raw = fp.read()
    except:
        print('[!] Could not open file "{}"'.format(sys.argv[1]))
        exit()

    l = raw.split('\n')[:-1]
    r = []
    tag_d = {}
    for i in l:
        a = re.search('<A HREF="(.*?)".*?">(.*?)</A>', i)
        if a:
            r.append(a.groups())
    for i in r:
        addr = i[0]
        name = i[1]
        tags = name.split(' ')
        if tags[0] not in tag_d:
            tag_d[tags[0]] = 1 
        else:
            tag_d[tags[0]] += 1
    for i in tag_d:
        print(i)

    print(len(r))
        

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('[*] Usage: {} bookmark.html'.format(__file__))
    else:
        main()

