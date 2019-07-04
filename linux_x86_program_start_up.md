http://www.dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html


execve() creates stack; pushes argc, argv & envp

1. _start:
(I actually cannot find it in some random C source)
pop argc into rsi & argv into rcx
push arguments for _libc_start_main on stack
    eax - 8th arg for alignment
    esp
    edx - Destructor of dynamic linker
    destructor of _start
    constructor of _start
    ecx - argv
    esi - argc
    entrypoint of main


2. _libc_start_main:
5. main with argc, argv and __environ
calls exit() with whatever main returns
- setuid setgid
- threading

3.  __libc_csu_init(=constructor), (__libc_csu_fini (=destructor)
get_pc_thunk -> PIC/-pic

4. _init
(gmon_start for profiling)
Constructor
_do_global_ctors_aux
Back to __libc_start_main to execute main



(Preamble ?)
