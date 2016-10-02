from LacOperon import *
from lib import Sensitivity
from modelPlot import plot
import datetime

lo = LacOperon()
dt =  0.0000125
t1 = 25
bp = 2
smplrt = int((t1/dt)/1000)
np, ns = lo.getSize()
names = lo.getNames()
en = Sensitivity(dt, t1, bp, lo.charFunc)

defParams = lo.pArr(1, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 26000)

defInitialVals = lo.iArr(0.4978354978306917, 0.27228876937802426, 0.5213396786687533, 0.004850296769185558,
    37479.45847464454, 18.011347105968394, 0.026789275794458223, 3.827040310495846, 0.19135105876949846)
defInitialVals = lo.iArr(0, 0, 0, 1, 0, 0, 0, 0, 0)
# bolus = None
bolus = lo.bArr(0, 0, 0, 0, 100000, 0, 0, 0, 0)

newParams = lo.pArr(1, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 15000)

defSSVal = en.calcSS(lo.getModel(defParams, defInitialVals, None))
print("-def-")
defData, defChars = en.calcChars(lo.getModel(defParams, defSSVal, bolus))
en.freeArr(defSSVal)

newSSVal = en.calcSS(lo.getModel(newParams, defInitialVals, None))
print("-new-")
newData, newChars = en.calcChars(lo.getModel(newParams, newSSVal, bolus))
en.freeArr(newSSVal)
se = en.deltaChars(newChars, defChars)

print(se)

fn = "lacopSensit_"+datetime.datetime.now().strftime("%I-%M-%S")

plot(defData, defChars, names, smplrt, "def_"+fn, [1])
plot(newData, newChars, names, smplrt, "new_"+fn, [1])

en.free(defData, ns)
en.free(newData, ns)