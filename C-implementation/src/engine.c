#include "all.h"

double** init(int numSpecies, int numPoints) {
    double** vals = malloc(sizeof (double*) * numSpecies);
    for (int i = 0; i < numSpecies; i++) {
        vals[i] = malloc(sizeof (double) * numPoints);
    }
    return vals;
}

void freeTime(void* arr) {
    free(arr);
}

void freeVals(void** arr, int numSpecies) {
    for (int i = 0; i < numSpecies; i++) {
        free(arr[i]);
    }
    free(arr);
}

double* getLast(double** vals, int numSpecies, int idx) {
    double* out = malloc(sizeof (double) * numSpecies);
    for (int i = 0; i < numSpecies; i++) {
        out[i] = vals[i][idx-1];
    }
    return out;
}

Results go(Model m, double dt, double t1) {
    int numPoints = (int)(t1 / dt);
    double** vals = init(m.numSpecies, numPoints);
    for (int i = 0; i < m.numSpecies; i++) {
        vals[i][0] = m.initVals[i];
    }

    for (int i = 1; i <= numPoints; i++) {
        double* last = getLast(vals, m.numSpecies, i);
        for (int j = 0; j < m.numSpecies; j++) {
            vals[j][i] = last[j] + ((*m.funcs[j])(m.params, last) * dt);
        }
        free(last);
    }

    double* time = malloc(sizeof (double) * numPoints);
    double e = 0;
    for (int i = 0; i <= numPoints; i++) {
        time[i] = e;
        e += dt;
    }

    Results out;
    out.values = vals;
    out.time = time;
    out.size = numPoints;
    return out;
}
