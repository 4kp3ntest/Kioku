#!/usr/bin/env python

import re


def print_ip(s):

    ipv4 = re.match('^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', s)
    if ipv4: #Check if one of octets has value > 255
        valid = 1
        for i in ipv4.groups():
            if int(i) > 255:
                valid = 0
        if valid:
            ret = 'IPv4'
        else:
            ret = 'Neither'

    elif re.match('^[abcdef\d]{1,4}(:[abcdef\d]{1,4}){0,7}$', s): #IPv6
        ret = 'IPv6'
    else: #Neither IPv4 nor IPv6
        ret = 'Neither'
    print(ret)


if __name__ == '__main__':
    print('Enter str to check:')
    print_ip(input())

