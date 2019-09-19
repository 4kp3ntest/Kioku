#!/usr/bin/env python
import subprocess
import sys
import os

# Colors whole bash output in specified color as easy as that:
# color_bash_output(String input, bcolor color)

formats = {
'dHEADER' : '\033[95m',

'default': '\033[94m',
'nier': '\033[96m',
'ausgegraut': '\033[90m',
'TEST': '\033[0;34m',
'OKGREEN': '\033[92m',
'WARNING': '\033[93m',
'FAIL': '\033[91m',
'ENDC': '\033[0m',
'BOLD': '\033[1m',
'UNDERLINE': '\033[4m'
}


#~~ MAIN ~~#
if __name__ == "__main__":
    default = formats.get('default', formats.get('default'))
    for line in sys.stdin:
        if len(sys.argv) == 2:
            default = formats.get(sys.argv[1], formats.get('default'))
        #sys.stdout.write(default + line)
        #Could also just use print:
        print(default + line, end='')

    #TODO Debug options
    #print(sys.argv)
