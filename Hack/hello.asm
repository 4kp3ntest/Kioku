BITS 64

jmp short one

two:
; ssize_t write(int fd, const void *buf, size_t count);
    xor     rdx,rdx         ;len of string
    push    0xf
    pop     rdx
    pop     rsi             ;pop String from Stack
    xor     rdi,rdi         ;1 for filedescriptor stdout
    inc     rdi                               
    xor     rax, rax        ;4 for syscall 4 - write
    push    4
    pop     rax
    syscall                 ; do syscall: write(1, string, 14)
; void _exit(int status);
    xor     rax, rax        ;syscall 60 - exit
    push    1
    pop     rax
;   int     0x80            ; do syscall:  exit(0)
    syscall

one:
    call two
    db "Hello RICK!!!", 0x0a, 0x0d  ; with newline and carriage return bytes
