#include <stdio.h>
#include "all.h"

extern Model sir;
double t1 = 20;
double dt = 0.5;

int main(int argc, char const *argv[]) {

    Results r = go(sir, dt, t1);
    for (int i = 0; i < r.size; i++) {
        char str[10];
        sprintf(str, "%f", r.time[i]);
        puts(str);
    }
    return 0;
}