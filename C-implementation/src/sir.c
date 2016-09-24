#include "all.h"
#include "sir.h"

double dSdt(double* params, double* last) {
    return -1*params[b]*last[S]*last[I];
}

double dIdt(double* params, double* last) {
    return (params[b]*last[S]*last[I])-(params[k]*last[I]);
}

double dRdt(double* params, double* last) {
    return params[k]*last[I];
}

ode funcs[3] = {&dSdt, &dIdt, &dRdt};
Model sir;

int getNumSpecies() {
  return nS;
}

int getNumParams() {
  return nP;
}

const char** getNames() {
  return names;
}


Model getModel(double* initVals, double* params) {
    if (initVals) {
        sir.initVals = initVals;
    } else {
        sir.initVals = defInitVals;
    }

    if (params) {
        sir.params = params;
    } else {
        sir.params = defParams;
    }

    sir.funcs = funcs;
    sir.numSpecies = nS;

    return sir;
}