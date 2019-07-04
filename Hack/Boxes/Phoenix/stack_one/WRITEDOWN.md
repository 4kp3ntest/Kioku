Nothing new in source, a char has the size of an int in C though.

Some problem with De Bruijn pattern:
right offset is off by factor 2 (32 instead of 64)
Don't know exactly why - tried variations in -a(rchitecture) flag, no change

Flag: $(python -c 'print("A"*64+"bYlI")')
