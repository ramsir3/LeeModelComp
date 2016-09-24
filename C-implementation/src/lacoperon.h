// species indecies
#define MR 0
#define R 1
#define R2 2
#define O 3
#define I 4
#define I2R2 5
#define MY 6
#define Y 7
#define YIex 8
// params indecies
#define OT 0
#define ksMR 1
#define ksR 2
#define k2R 3
#define kn2R 4
#define kr 5
#define knr 6
#define kdr1 7
#define kndr1 8
#define kdr2 9
#define kndr2 10
#define ks1MY 11
#define ks0MY 12
#define ksY 13
#define kp 14
#define knp 15
#define kft 16
#define kt 17
#define lMR 18
#define lMY 19
#define lR 20
#define lR2 21
#define lY 22
#define lYIex 23
#define lI2R2 24
#define Iex 25

const int nS = 9;
const int nP = 26;
// values
double defParams[26] = {1, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 25000};

double defInitVals[9] = {0, 0, 0, 1, 0, 0, 0, 0, 0};

const char* names[9] = {
    "MR",
    "R",
    "R2",
    "O",
    "I",
    "I2R2",
    "MY",
    "Y",
    "YIex"
};