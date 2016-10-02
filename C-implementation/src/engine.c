#include "all.h"

double** init(int numSpecies, int numPoints) {
    double** vals = malloc(sizeof (double*) * numSpecies);
    for (int i = 0; i < numSpecies; i++) {
        vals[i] = malloc(sizeof (double) * numPoints);
    }
    return vals;
}

void freeArr(void* arr) {
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

double* perturb(double* vals, double* bolus, int numSpecies) {
  for (int i = 0; i < numSpecies; i++) {
      vals[i] += bolus[i];
  }
  return vals;
}

double* calcSS(Model m, double dt) {
    double* last = m.initVals;
    double* vals = (double*)malloc(sizeof (double) * m.numSpecies);
    double* dVal = malloc(sizeof (double) * m.numSpecies);
    int* doneArr = malloc(sizeof (int) * m.numSpecies);
    int done = 0;
    int i = 0;
    // for (int x = 0; x < m.numSpecies; x++) {
    //     printf("%s%f\n","c lastsdf: ", last[x]);
    // }
    // printf("%d\n", m.numParams);
    // for (int x = 0; x < m.numParams; x++) {
    //     printf("%s%f\n","c params: ", m.params[x]);
    // }

    do {
        done = 1;
        for (int j = 0; j < m.numSpecies; j++) {
            dVal[j] = ((*m.funcs[j])(m.params, last) * dt);
            vals[j] = last[j] + dVal[j];
            doneArr[j] = (dVal[j] < 0.00000000001 && dVal[j] > -0.00000000001);
        }
        for (int j = 0; j < m.numSpecies; j++) {
            done = done && doneArr[j];
        }
        // if (i % 10000000 == 0) {
        //     for (int j = 0; j < m.numSpecies; j++) {
        //         printf("%d%s%d%s%.32f\n", j, " : ", doneArr[j], " : ", dVal[j]);
        //     }
        // }
        last = vals;
        i++;
    } while (!done);
    free(dVal);
    free(doneArr);
    // if (done) {
    //     printf("%s%d\n","cycles:", i);
    // }
    // for (int i = 0; i < m.numSpecies; i++) {
    //     printf("%s%.32f\n", "c: ", vals[i]);
    // }
    return vals;
}

Results go(Model m, double dt, double t1, int bp) {
    int numPoints = (int)(t1 / dt);
    double** vals = init(m.numSpecies, numPoints);
    for (int i = 0; i < m.numSpecies; i++) {
        vals[i][0] = m.initVals[i];
    }

    for (int i = 1; i <= numPoints; i++) {
        double* last = getLast(vals, m.numSpecies, i);
        if (i == bp) {
            last = perturb(last, m.bolus, m.numSpecies);
        }
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
    out.vals = vals;
    out.time = time;
    out.size = numPoints;
    return out;
}
