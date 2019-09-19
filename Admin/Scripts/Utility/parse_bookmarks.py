#!/usr/bin/python3

import sys
import re
import string
import ipdb

"""
Parse a bookmarks.html file by the provided tags
Group and structurize them together by common tags (order is important atm)

param arg:  bookmark.html file 
returns:    BOOKMARKS.md file
"""
def add_to_nested_list_at_index(nested_list, index_list, sub_list):
    # Goto right index
    nested_list = eval(sublist_from_index(index_list))
    # Append sub_list
    nested_list.append(sub_list)

def sublist_from_index(index_list):
    """
    returns:            String that evaluates to part of nested_list
    """
    ret = 'nested_list'
    for i in index_list:
        ret += '[{}]'.format(i)

    return ret

def find_tag_index(index, tag, index_list, nested_list):
    """
    Function receives a specific tag searches for it in nested_list
    and returns its index if found, 0 otherwise

    param nested_list:  structurized representation of entries
    param index_list:   starting point searching in nested list (previous tag found)
    param index:
    param tag:        

    returns:            index of the already present tag in nested_list, 0 if not found
    """
    ret = -1 
    nested_list = eval(sublist_from_index(index_list))

    for i in range(len(nested_list)):
        # Return Index if found
        if tag == nested_list[i][0]:
            ret = i
            break

    return ret

def convert_tag_list_to_nested_list(tag_list):
    """
    Convert a list of tags to the corresponding nested tags 
    returns: list with this format [tag1, [tag11, [tag111]]] 
    """
    try:
        ret = [tag_list[0]]
        for i in range(1, len(tag_list)):
            eval('ret{}.append([tag_list[i]])'.format((i-1)*'[1]'))
        return ret
    except Exception as err:
        print(err)
        

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
    for entry in polished_entries[1:]:
        tags = entry[1] #list
        name = entry[2] #string
        index_list = []

        print(entry)
        for i, val in enumerate(tags):
            new_index = find_tag_index(i, val, index_list, nested_list)
            if new_index != -1:
                index_list.append(new_index)
            else: 
                # Add (unique part of) tags+name @ right index in nested_list
                unique_tag_list = convert_tag_list_to_nested_list(tags[i:]+[name])
                add_to_nested_list_at_index(nested_list, index_list, unique_tag_list)
                break
    
    ipdb.set_trace(context=7)
    print('[*] Bookmark count: {}'.format(len(polished_entries)))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('[*] Usage: {} bookmark.html'.format(__file__))
    else:
        main()

