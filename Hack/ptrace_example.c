#include <stdio.h>
#include <sys/ptrace.h>

int main()
{
    if (ptrace(PTRACE_TRACEME, 0, 1, 0)) 
    {
        printf("don't trace me !!\n");
        return 1;
    }
    // normal execution
    return 0;
}
