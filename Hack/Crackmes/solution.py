#!/usr/bin/python2.7

from pwn import *

def get_num_links(n):
    edx = n^123
    edx += n^321
    ecx = edx * 21309
    edx = 1374389535
    #imul edx (only the first 32 bit are saved in edx)
    edx *= ecx
    edx = int(bin(edx)[:-32], 2)
    edx = edx >> 5 
    eax = ecx >> 31
    edx -= eax
    edx = edx*100 
    ecx -= edx

    return ecx

