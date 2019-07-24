#!/usr/bin/python3

import sys
import re
import string

"""
The idea is to parse my bookmarks by the provided tags to better group and structurize them together

reads a bookmark.html file as cmd arg and creates a BOOKMARKS.md file from it
"""


def find_tag_index(index, value, index_list, nested_list):
    if not nested_list: #first entry
        ret = 0
    else:
        n = len(index_list)
        for i in 



    return ret

def convert_tag_list_to_nested_list(tag_list):
    """
    Convert a list of tags to the corresponding nested tags 
    [[tag1, [tag11, tag12], [tag2]] 
    """
    N = len(tag_list)
    s1, s2 = '"', '.format('

    for i in range(n):
        s1 += '[{},'
        s2 += 'tag_list['+str(i)+'], '

    ret = eval(s1+']'*n+'"'+s2+')')
    return ret
        


def main():
    try:
        with open(sys.argv[1]) as fp:
            raw = fp.read()
    except:
        print('[!] Could not open file "{}"'.format(sys.argv[1]))
        exit()

    """
    Search raw text of bookmarks.html for URLs and my description
    Create a list like so
    [[URL, [tag0, tag1], name], ... ]
    """
    raw_lines = raw.split('\n')[:-1]
    raw_entries = []
    polished_entries = []
    for line in raw_lines:
        # Regex for URL and my custom name/description (TUPLE !)
        tmp = re.search('<A HREF="(.*?)".*?">(.*?)</A>', line)
        if tmp:
            raw_entries.append(tmp.groups())
    for i, val in enumerate(raw_entries):
        tags = []
        words = val[1].split(' ')
        for i, val in enumerate(words):
            if not val.isupper():
                tags.append(val)
            else:
                name = ' '.join(words[i:])
                break
        polished_entries.append([raw_entries[i][0], tags, name])

    """
    Create nested list from all entries with following format
    [[tag0, [tag00, [tag000, tag001], tag01]], [tag1], [tag2, [tag20]]] 
    """
    nested_list = []
    for entry in polished_entries:
        tags = entry[1] #list
        name = entry[2] #string
        index_list = []

        for i, val in enumerate(tags):
            new_index = find_tag_index(i, val, index_list, nested_list)
            if new_index:
                index_list.append(new_index)
            else: 
                #TODO index_list beachten
                nested_list.append(convert_tag_list_to_nested_list(tags))
                break
    

        tmp = convert_tag_list_to_nested_list(tags)
        print(tmp)
    
    print('[*] Bookmark count: {}'.format(len(polished_entries)))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('[*] Usage: {} bookmark.html'.format(__file__))
    else:
        main()

