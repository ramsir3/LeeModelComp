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


Model getModel(double* initVals, double* params) {
    sir.names = names;

    if (initVals) {
        sir.initValues = initVals;
    } else {
        sir.initValues = definitValues;
    }

    if (params) {
        sir.params = params;
    } else {
        sir.params = defparams;
    }

    sir.funcs = funcs;
    sir.numSpecies = nS;

    return sir;
}