#!/bin/bash

cat << EOD
if [[ a -@ b ]]; then
do ...
----------file options------------------------------------------------------
    -a      |   True if b exists
    -d      |   True if b exists and is a dictionary
    -r      |   True if b exists and is readable
    -s      |   True if b exists and has a size greater than zero
    -w      |   True if b exists and is writeable
    -x      |   True if b exists and is executeable
    -O      |   True if b exists and is owned by effective user id
    -G      |   True if b exists and is owned by effective group id
    -S      |   True if b exists and is a socket
    -N      |   True if b exists and has been modified since last read
  a -nt b   |   True if a is NEWER than b
  a -ot b   |   True if a is OLDER than b

----------string options----------------------------------------------------
    -z b    |   True if the length of b is zero
    -n b    |   True if the length of b is NOT zero
  a == b    |   True if strings are equal
  a != b    |   True if strings are NOT equal
  a < b     |   True if a kommt im Alphabet vorher
  a > b     |   True if b kommt im Alphabet vorher
----------------------------------------------------------------------------
EOD


