from lib import LacOperon, Sensitivities, SIR
from charFuncs import *

# sir = SIR()

# dt = 0.01
# t1 = 100

# defParams =  sir.pArr(0.5, 0.333)
# defInitialVals = None

# newParams = sir.pArr(0.75, 0.333)

# s = Sensitivities(sir, defParams, defInitialVals, dt, t1, sirCharFunc)
# out = s.calcSensitivity(newParams, None)
# print out

lo = LacOperon()

dt =  0.0000125
t1 = 80
defParams = lo.pArr(1, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 25000)
defInitialVals = lo.iArr(0, 0, 0, 1, 0, 0, 0, 0, 0)

newParams = lo.pArr(2, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 25000)

s = Sensitivities(lo, defParams, defInitialVals, dt, t1, lacOpCharFunc)
out = s.calcSensitivity(newParams, None)
print out