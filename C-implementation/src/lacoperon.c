#include "all.h"
#include "lacoperon.h"

//   equation(3)
double dMRdt(double* params, double* last) {
    return params[ksMR]
           -(params[lMR]*last[MR]);
}

//   equation(4)
double dRdt(double* params, double* last) {
    return (params[ksR]*last[MR])
           -(2*params[k2R]*(last[R]*last[R]))
           +(2*params[kn2R]*last[R2])
           -(params[lR]*last[R]);
}

//   equation(5)
double dR2dt(double* params, double* last) {
    return (params[k2R]*(last[R]*last[R]))
           -(params[kn2R]*last[R2])
           -(params[kr]*last[R2]*last[O])
           +(params[knr]*(params[OT]-last[O]))
           -(params[kdr1]*last[R2]*(last[I]*last[I]))
           +(params[kndr1]*last[I2R2])
           -(params[lR2]*last[R2]);
}

//   equation(6)
double dOdt(double* params, double* last) {
    return -(params[kr]*last[R2]*last[O])
           +(params[knr]*(params[OT]-last[O]))
           +(params[kdr2]*(params[OT]-last[O])*(last[I]*last[I]))
           -(params[kndr2]*last[O]*last[I2R2]);
}

//   equation(7)
double dIdt(double* params, double* last) {
    return -(2*params[kdr1]*last[R2]*(last[I]*last[I]))
           +(2*params[kndr1]*last[I2R2])
           -(2*params[kdr2]*(params[OT]-last[O])*(last[I]*last[I]))
           +(2*params[kndr2]*last[O]*last[I2R2])
           +(params[kft]*last[YIex])
           +(params[kt]*(params[Iex]-last[I]))
           +(2*params[lI2R2]*last[I2R2])
           +(params[lYIex]*last[YIex]);
}
//   equation(8)
double dI2R2dt(double* params, double* last) {
    return (params[kdr1]*last[R2]*(last[I]*last[I]))
           -(params[kndr1]*last[I2R2])
           +(params[kdr2]*(params[OT]-last[O])*(last[I]*last[I]))
           -(params[kndr2]*last[O]*last[I2R2])
           -(params[lI2R2]*last[I2R2]);
}

//   equation(9)
double dMYdt(double* params, double* last) {
    return (params[ks0MY]*(params[OT]-last[O]))
           +(params[ks1MY]*last[O])
           -(params[lMY]*last[MY]);
}

//   equation(10)
double dYdt(double* params, double* last) {
    return (params[ksY]*last[MY])
           +((params[kft]+params[knp])*last[YIex])
           -(params[kp]*last[Y]*params[Iex])
           -(params[lY]*last[Y]);
}
//   equation(11)H
double dYIexdt(double* params, double* last) {
    return -((params[kft]+params[knp])*last[YIex])
           +(params[kp]*last[Y]*params[Iex])
           -(params[lYIex]*last[YIex]);
}

Model lacoperon;
ode funcs[9] = {&dMRdt, &dRdt, &dR2dt, &dOdt, &dIdt, &dI2R2dt, &dMYdt, &dYdt, &dYIexdt};

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
        lacoperon.initValues = initVals;
    } else {
        lacoperon.initValues = definitValues;
    }

    if (params) {
        lacoperon.params = params;
    } else {
        lacoperon.params = defparams;
    }

    lacoperon.funcs = funcs;
    lacoperon.numSpecies = nS;

    return lacoperon;
}