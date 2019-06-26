http://www.dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html


execve() creates stack and pushes argc, argv and envp to it 

_start:
pop argc into rsi
save argv into rcx
push arguments for _libc_start_main on stack
esp
edx - Destructor of dynamic linker
    destructor of _start
    constructor of _start
ecx - argv
esi - argc
entrypoint of main


_libc_start_main:
calls main with argc, argv and __environ
calls exit() with whatever main returns
- setuid setgid
- threading

 __libc_csu_init(=constructor), (__libc_csu_fini (=destructor)
get_pc_thunk -> PIC/-pic

_init


Constructor
_do_global_ctors_aux


Back to __libc_start_main to execute main



Preamble
