#include "process-bar.h"
#include <stdio.h>

char _result[110];

const char* processBar(double current, double duration) {
    // 计算百分比
    double percent = current / duration * 100;
    int now = percent;

    int index = 0;
    index += sprintf(_result, "%5.1lf", percent);
    index += sprintf(&_result[index], "%s", "% [");

    int i = 0;
    for (; i < now; ++i) {
        _result[index++] = '=';
    }
    for (; i < 100; ++i) {
        _result[index++] = ' ';
    }

    _result[index++] = ']';
    _result[index] = '\0';

    return _result;
}
