# Basics
## start with aas to analyze functions and strings
### s to seek
### i for info
    # il for libraries
    # iz for strings
    # ii for imports
### pd for print dissassembly
    # pdf for function
### dr to show register
### f to flag/bookmark parts

# Exploration
## Memory location of function
?v sym.imp.puts
?v reloc.puts
dmi libc puts
## find where strings reference to
axt @@ str*
## show all elements of imports namespace
fs imports; f 
    dm. # memory location of current map
### search in all memory maps:
e search.in = dbg.maps
/ /bin/sh #to search
## Show hex of reg
px 44 rbp
pad d1c0 # disassemble hex 
## find ROP gadgets
/R sub ebx, 10 or whatever

# Interface commands
## export as python code
pcp 44 @ 0x4007a0

## Debug Mode 
### Debug continue
dcu main
open with -d flag or issue ood/doo from r2 shell
### Debug Register
dr rdi
#### Hardware breakpoint 
drx 1 0x0040066d 1 x|w|r
#### List conditional jumps
drc
##### Set Zero flag
dr zf=1
### Analyse
#### analyse Refs
axf/axt
#### show variable
afvd
.afvd <var>
#### rename variable
afvn new old

### Print hex register (STACK)
pxr @ rsp

# Visual mode
    use V to get there
    use R to change color theme
Start execution with s/S or F7/F8; F9 to continue


# Craft exploit sequences with De Bruijn Sequence
#### ragg2 -P 100 -r > pattern.txt
## see also 
    # rahash2 to do all sorts of substitutions like rot13
    # rarun2


