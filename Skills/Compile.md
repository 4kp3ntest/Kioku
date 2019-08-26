# GCC
gcc -o output.bin input.c
### Shellcode
nasm somefile.asm
### Assembly from C
gcc -S hello.c
### Object file from Assembly
nasm -f elf64 assembly.s
### Link
ld -S assembly.o

## Flags
#### Canary
-fno-stack-protector
-fno-pic
-no-pie
#### NX Bit
-z execstack

# Exploit Mitigation
### ASLR
/proc/sys/kernel/randomize_va_space 
0 - No randomization
1 - Shared libs, stack, heap, mmap() & VDSO are random
2 - all in 1 + brk()


# Linker
## by Ian Lance Taylor
### part 2
symbols, relocations refer to content by addresses
program linker: creates table containing all symbols; 
dynamic linker: substitutes empty portions for relocations with appr. addr

### part 3
Address Spaces == 
Shared lib has BASE addr that get's adjusted when copied into vaddr space of prog
Object File Formats - record oriented & section oriented

### part 4
Shared Libraries (ELF vs DLL)
PIC minimized relocs that need to be done on prog startup
PLT list to non-static functions; special entry.plt in .o file
GOT for global and static variables
Basically we sacrifice some performance during runtime (to lookup stuff in PLT & GOT) for almost no relocations by dynamic linker and therefore faster start up

