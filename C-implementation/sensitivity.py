from LacOperon import *
from lib import Sensitivity
from util import c_arr2str, sensitivity2str
from modelPlot import plot
import datetime

lo = LacOperon()
dt =  0.000005
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
defInitialVals = lo.iArr(0, 0, 0, 1, 0, 0, 0, 0, 0)
# bolus = None
bolus = lo.bArr(5, 0, 0, 0, 0, 0, 0, 0, 0)

newParams = lo.pArr(1, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 15000)

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
    defParams[i] = scaledp(i)
    newSSVal = en.calcSS(lo.getModel(defParams, defInitialVals, None))
    newData, newChars = en.calcChars(lo.getModel(defParams, newSSVal, bolus))
    en.free(newData, ns)
    en.freeArr(newSSVal)
    se = en.deltaChars(newChars, defChars)
    f.write("\nparam "+str(i)+": ("+param_names[i]+") =,"+str(defParams[i])+'\n')
    defParams[i] = old
    # print("def:",c_arr2str(defParams))
    f.write(sensitivity2str(se, names)+'\n')
    onePls = list()
    for i in xrange(len(se)):
        seSp = se[i]
        if i == 0:
            onePls += [seSp[0][0]] + [seSp[1][2]]
        else:
            onePls += [seSp[0][0]] + seSp[1]
    print(onePls)
    matrix.append(onePls)

f.close()

matrix = [[matrix[i][j] for i in xrange(len(matrix))] for j in xrange(len(matrix[0]))]
matrixf = open("charmatrix.py", 'w')
matrixf.write("matrix = "+str(matrix))
matrixf.close()
# fn = "lacopSensit_"+datetime.datetime.now().strftime("%I-%M-%S")

# plot(defData, defChars, names, smplrt, "def_"+fn, None)
# plot(newData, newChars, names, smplrt, "new_"+fn, [1])
# print(matrix)
en.free(defData, ns)
# en.free(newData, ns)