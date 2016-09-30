#include <stdio.h>
#include "all.h"

extern Model sir;
double t1 = 20;
double dt = 0.5;

int main(int argc, char const *argv[]) {

    Results r = go(sir, dt, t1, -1);
    for (int i = 0; i < r.size; i++) {
        printf("%s\n", "test");
        double* one = r.vals[0];
        printf("%s\n", "test");
        printf("%f\n", one[0]);
    }
    return 0;
}