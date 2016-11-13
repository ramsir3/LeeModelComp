from LacOperon import *
from lib import Sensitivity
from util import c_arr2str, sensitivity2str
from modelPlot import plot
from correlations import calcCorMatrix
import datetime

lo = LacOperon()
dt =  0.0000025
t1 = 45
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
# defInitialVals = lo.iArr(0, 0, 0, 1, 0, 0, 0, 0, 0)
# bolus = None
bolus = lo.bArr(5, 0, 0, 0, 0, 0, 0, 0, 0)

newParams = lo.pArr(0.154977514043, 1.16462169406, 7.03433844184, 154.746207648, 0.00019537219059, 7118.81963368, 24.6690045197, 2.38337847508e-07, 4.11519429287, 1.95971542799e-07, 47383.95692, 0.387249488649, 0.0220698650347, 22.6682218121, 0.00422368688352, 0.958937842327, 13966.6093417, 0.84513174251, 6.1302738193, 3.82796984736, 0.0811790521043, 0.0740019990288, 0.0443714858756, 0.042983581708, 6.00254638463, 37610.8755213)

def scaledp(ind):
    scale = 1.2
    return scale*defParams[i]

def newp(ind):
    return newParams[i]

defSSVal = en.calcSS(lo.getModel(defParams, defInitialVals, None))
print("-def-")
defData, defChars = en.calcChars(lo.getModel(defParams, defSSVal, bolus))
en.freeArr(defSSVal)

matrix = list()
f = open("results/sensitivity_results_"+datetime.datetime.now().strftime("%I-%M-%S")+".csv", 'w')
f.write("default params\n" + c_arr2str(defParams)+'\n')
for i in range(np):
    print("-new-"+str(i))
    old = defParams[i]
    defParams[i] = newp(i)
    newSSVal = en.calcSS(lo.getModel(defParams, defInitialVals, None))
    newData, newChars = en.calcChars(lo.getModel(defParams, newSSVal, bolus))
    en.free(newData, ns)
    en.freeArr(newSSVal)
    se = en.deltaChars(newChars, defChars)
    f.write("\nparam "+str(i)+": ("+param_names[i]+") =,"+str(defParams[i])+'\n')
    defParams[i] = old
    # print("def:",c_arr2str(defParams))
    f.write(sensitivity2str(se, names))
    matrix.append(makeSensitivityList(se))

f.close()
en.free(defData, ns)


matrix = [[matrix[i][j] for i in xrange(len(matrix))] for j in xrange(len(matrix[0]))]
matrix = makeSignChanges(matrix)
calcCorMatrix(matrix, "cor" + datetime.datetime.now().strftime("%I-%M-%S"))