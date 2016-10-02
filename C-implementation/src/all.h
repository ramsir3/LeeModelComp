#include <stdlib.h>
#include <stdio.h>

typedef double (*ode)(double[], double[]);

typedef struct {
    double* initVals;
    double* params;
    double* bolus;
    ode* funcs;
    int numSpecies;
    int numParams;
} Model;

typedef struct {
    double** vals;
    double* time;
    int size;
} Results;

double** init(int, int);
double* getLast(double**, int, int);
Results go(Model, double, double, int);
int getNumSpecies();
int getNumParams();
double* preturb(double*, double*, int);
double* calcSS(Model, double);
Model getModel(double*, double*, double*);
