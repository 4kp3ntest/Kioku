#! /usr/bin/python3

# The usual culprits that will break a payload.
forbidden = '\x00\t \r\n\xff'

chars = b''
for i in range(0, 256):
    char = chr(i)
    if char in forbidden:
        continue
    # Must use latin1 encoding rather than the default utf-8.
    chars += char.encode('latin1')

with open('chars.txt', 'wb') as f:
    f.write(chars)

