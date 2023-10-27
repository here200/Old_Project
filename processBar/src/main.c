#include <stdio.h>
#include <windows.h>
#include "util/process-bar.h"

int main()
{
    int i = 0;
    int duration = 233;

    for (; i < duration+1; ++i) {
        printf("%s\r", processBar(i, duration));
        Sleep(80);
    }

    return 0;
}
