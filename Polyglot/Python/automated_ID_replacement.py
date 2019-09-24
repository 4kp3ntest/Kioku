#!/usr/bin/python3

import subprocess
import string
import sys
import re
import pytesseract
import pandas as pd
from PIL import Image
from difflib import SequenceMatcher

"""
Author: Andreas.Kellerer@comlet.de
"""

TOPFOLDER = 'suite_AEF_Part6'
XML = 'UserPromptsConfigPart6.xml'
XLSX = 'AutomationDialogIds.xlsx'
notebook = []
debug = False
folders = [
#        'tst_11783-06-001',    #FINISHED
#        'tst_11783-06-003',    #FINISHED  
#        'tst_11783-06-005',    #FINISHED
#        'tst_11783-06-009',    #ERROR
#        'tst_11783-06-011',    #RUN 
#        'tst_11783-06-013',    #RUN
#        'tst_11783-06-015',    #ALREADY SUBSTITUTED
#        'tst_11783-06-031',
#        'tst_11783-06-033',
#        'tst_11783-06-035',
#        'tst_11783-06-037',
         'tst_11783-06-201-01',
#        'tst_11783-06-201-04',
#        'tst_11783-06-201-05'
]


#0x0 Load stuff
def load_stuff():

    print('[*] Loading stuff')
    # Load xml file
    with open (XML) as fp:
        xml = fp.read()
    xl = pd.ExcelFile(XLSX)
    # Load excel sheets
    # Only two sheets - no need for loop
    df0 = xl.parse(xl.sheet_names[0])
    df1 = xl.parse(xl.sheet_names[1])
    # Put everything in temporary text file 'cause no time for excel magic
    df0.to_csv('tmp0.txt')
    df1.to_csv('tmp1.txt')
    with open('tmp0.txt') as fp:
        xlsx = fp.read()
    with open('tmp1.txt') as fp:
        xlsx += fp.read()
    # Sanitize escape sequences not present in screenshots for better matches in 0x4
    xlsx = xlsx.replace('\"', '')
    return xml, xlsx

#0x1 Parse every test.py 
def find_old_ids(fname):

    print('    [*] Find old IDs')
    with open('{}/{}/test.py'.format(TOPFOLDER, fname)) as fp:
        raw = fp.read()
        tmp = re.findall('id == (\d{1,9})[ \:]', raw)
    # ID 0 not valid
    tmp.remove('0')
    return tmp, raw 

#0x2 map with the corresponding screenshot file from XML
def add_screenshot_fn_to_nb(tmp, xml):

    global notebook
    for i in tmp:
        reg = '<screenshot>(.*?)</screenshot>\s{0,20}<identifier>' + str(i) + '</identifier>'
        notebook_entry = [i, re.findall(reg, xml)[0]]
        if debug:
            print('{} Getting name of screenshot file for ID'.format('%'*10))
            print('{} {}\n\n'.format('%'*10, notebook_entry))
        notebook.append(notebook_entry)

#0x3 Get string from screenshot - step may take a while
def add_screenshot_str_to_nb(i):

    global notebook
    im = Image.open(notebook[i][1])
    text = pytesseract.image_to_string(im, lang='eng')
    if debug:
        print('{} Text of screenshot is:\n {}\n\n'.format('%'*10, text))
    notebook[i].append(text)

#0x4 Loop every line of Excel and find best matching substring with text from screenshot
#notebook = [[old_id, ss_fn, text_ss], ...]
def find_best_match_in_raw_excel(i, xlsx):

    global notebook
    xlsx_l = xlsx.split('\n')
    matches = []
    match_min_len = 7 #arbitrary
    # For every row in exel check the longest substr with screenshot text
    for row in xlsx_l:
        ss_text = notebook[i][2] 
        ss_text = ' '.join(ss_text.split('\n')[1:]) # Do not use title of window
        match = SequenceMatcher(None, row, ss_text)\
                .find_longest_match(0, len(row), 0, len(ss_text))
        if match.size > match_min_len:
            if debug:
                tmp = row[match.a:match.a+match.size]
                print('{} Best match atm is: {}'.format('%'*10, tmp))
            match_min_len = match.size
            matches = [row]
        elif match.size >= match_min_len:
            matches.append(row)
    if debug:
        print('{} The found matches are:\n'.format('%'*10))
        print('{}'.format(matches))
        print('\n\n')
    return matches

#0x5 Extract the new ID from all_matches and add to notebook
#   1. Find all the 10 len digits 
#   2. Check if only one ID - finish if yes, step 3 if not
#   3. Sort out IDs that don't correspond to the right testcase file
#   4. If still more than one left add a note in comments
def find_new_id_from_excel(i, text_matches, fname):

    global notebook
    uniq_dialogID = ['NO DIALOGID FOUND']
    string = '\n'.join(text_matches)
    dialogIDs = re.findall('\d{10}', string) #1.

    if len(set(dialogIDs)) == 1:
        uniq_dialogID = [dialogIDs[0]] #2.
        if debug: print('{} DialogID {} is uniqe - no prob here!\n'.format('%'*10, dialogIDs))

    else: #3.
        if debug: print('{} DialogID is NOT uniqe! Check with folder.\n{}'.format('%'*10, dialogIDs))
        match_min_len = 0
        matches = []
        for j in text_matches: 
            match = SequenceMatcher(None, j, fname)\
                .find_longest_match(0, len(j), 0, len(fname))

            if match.size > match_min_len:
                match_min_len = match.size
                matches = [j]
                
            elif match.size == match_min_len:
                matches.append(j)
        string = '\n'.join(matches)
        dialogIDs = re.findall('\d{10}', string)
        if len(set(dialogIDs)) == 1:
            uniq_dialogID = [dialogIDs[0]]

            if debug: print('{} DialogID {} is unique -\
                     no prob here!\n'.format('%'*10, uniq_dialogID))

        elif len(set(dialogIDs)) > 1: #4.
            uniq_dialogID = dialogIDs

            if debug: 
                print('{} No distinct DialogID could be choosen -\
                    manuall intervention required!'.format('%'*10, uniq_dialogID))
                print('{} Candidates: {}'.format('%'*10, dialogIDs))
    notebook[i].append(uniq_dialogID)

#0x6 Replace old IDs with a str containing new ID
#   1. Actuall replacement
#   2. Add comments for evaluation
#notebook = [[old_id, ss_fn, text_ss, new_id], ...]
# remember raw from 0x1?
def reg_replace(m, i): return m.group().replace(m.groups()[0], "'{}'".format(i[3][0]))

def replace_old_ids(raw):

    print('    [*] Write file with substituted IDs and debug comments to file ')
    global notebook
    output = raw
    for i in notebook:
        reg = 'id == (' + str(i[0]) + ')[ \:]'
        # Use lambda function to pass additional arg to re.sub function
        output = re.sub(reg, lambda m: reg_replace(m, i), output)
    # Iterate through lines and put comments behind new IDs
    # Use (unchanged) raw to find already substituted IDs in output 
    # (Add comments in output)
    output_l = output.split('\n')
    raw_l = raw.split('\n')
    for i, line in enumerate(output_l):
        old_id_cmt = []
        duplicate_id_cmt = []
        for j in notebook:
            reg = 'id == '+str(j[0])+'[ \:]'
            id_on_line = re.search(reg, raw_l[i])
            if id_on_line:# Line with new ID -> add comments
                old_id_cmt.append(int(j[0])) 
                if len(j[3]) > 1: # more than one ID -> add comment
                    duplicate_id_cmt.append('old ID {} has multiple fitting new IDs: {}'
                            .format(j[0], ', '.join(j[3])))
        if old_id_cmt:
            old_id_cmt.sort()
            comment = ' # {}'.format(', '.join(list(map(str, old_id_cmt))))
            if duplicate_id_cmt:
                comment += ' FIXME {}'.format(';  '.join(duplicate_id_cmt))
            output_l[i] = line + comment
    return '\n'.join(output_l)
    
def main():

    global debug
    xml, xlsx = load_stuff()
    # Check only specific ID and provide extensive output
    search_id = False
    if len(sys.argv) > 1:
        if sys.argv[1].isdecimal():
            search_id = sys.argv[1]
        debug = True

    for folder in folders:
        print('[@] running on folder: {}'.format(folder))
        tmp, raw_txt = find_old_ids(folder)
        if search_id:
            tmp = [search_id]

        add_screenshot_fn_to_nb(tmp, xml)

        for i in range(len(notebook)):
            add_screenshot_str_to_nb(i)
            screenshot_text_matches = find_best_match_in_raw_excel(i, xlsx)
            find_new_id_from_excel(i, screenshot_text_matches, folder)
            tmp = notebook[i]
            print('\n{}: {}'.format(tmp[0], ''.join(tmp[2].split('\n')[2:5]))) 


        if not debug:
            output = replace_old_ids(raw_txt)
            fname = 'AutomatedReplaced/test_'+'-'.join(folder.split('-')[1:])+'.py'
            with open(fname, 'w') as fp:
                fp.write(output)


if __name__ == '__main__':
    main()

