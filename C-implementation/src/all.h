#include <stdlib.h>

typedef double (*ode)(double[], double[]);

typedef struct {
    const char** names;
    double* initValues;
    double* params;
    ode* funcs;
    int numSpecies;
    int numParams;
} Model;

typedef struct {
    double** values;
    double* time;
    int size;
} Results;

double** init(int, int);
double* getLast(double**, int, int);
Results go(Model, double, double);
int getNumSpecies();
int getNumParams();