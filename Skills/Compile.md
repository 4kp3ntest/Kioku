# Ian Lance Taylor
## part 2
symbols, relocations refer to content by addresses
program linker: creates table containing all symbols; 
dynamic linker: substitutes empty portions for relocations with appr. addr

## part 3
Address Spaces == 
Shared lib has BASE addr that get's adjusted when copied into vaddr space of prog
Object File Formats - record oriented & section oriented

## part 4
Shared Libraries (ELF vs DLL)
PIC minimized relocs that need to be done on prog startup
PLT list to non-static functions; special entry.plt in .o file
GOT for global and static variables
Basically we sacrifice some performance during runtime (to lookup stuff in PLT & GOT) for almost no relocations by dynamic linker and therefore faster start up

