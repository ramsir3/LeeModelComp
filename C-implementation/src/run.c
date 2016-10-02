#include "all.h"

double t1 = 20;
double dt = 0.0000125;

int main(int argc, char const *argv[]) {
    void* null = 0;
    Model lacoperon = getModel(null, null, null);
    double* r = calcSS(lacoperon, dt);
    // for (int i = 0; i < 9; i++) {
    //     printf("%f\n", r[i]);
    // }
    free(r);
    return 0;
}