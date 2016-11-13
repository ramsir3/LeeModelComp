from LacOperon import *
from lib import Sensitivity
from util import c_arr2str, sensitivity2str
import random as r
import math as m
# from timeout import *
import pdb

lo = LacOperon()
dt =  0.00000125
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
bolus = lo.bArr(10, 0, 0, 0, 0, 0, 0, 0, 0)

defSSVal = en.calcSS(lo.getModel(defParams, defInitialVals, None))
print("-def-")
defData, defChars = en.calcChars(lo.getModel(defParams, defSSVal, bolus))
en.freeArr(defSSVal)
en.free(defData, ns)

def copyParams(arr):
    out = lo.pArr(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    for i in xrange(len(arr)):
        out[i] = arr[i]
    return out

def scaledp(randRange):
    lo, hi = randRange
    # print("lo:",lo)
    lo = m.log(lo)
    hi = m.log(hi)
    out = m.exp(r.uniform(lo, hi))
    # print(out)
    return out

def runCalc(nwp):
    print("calcing")
    # timestr = datetime.datetime.now().strftime("%I-%M-%S")
    pdb.set_trace()
    newSSVal = en.calcSS(lo.getModel(nwp, defInitialVals, None))
    print("found ss")
    newData, newChars = en.calcChars(lo.getModel(nwp, newSSVal, bolus))
    en.free(newData, ns)
    en.freeArr(newSSVal)
    # print("exited c")

    se = en.deltaChars(newChars, defChars)
    selist = makeSensitivityList(se)
    return selist

def consistant(new):
    for x in xrange(len(new)):
        if new[x] == None:
            return False
    return True

def recursiveSearch(paramState, xf, err):
    print("start recursing")
    print('['+c_arr2str(paramState)+']')
    print("error:", err)
    if err and err < 0.1 and err >= 0: #error threshold
        return paramState
    old_params = copyParams(paramState)
    print("copied")
    xf *= 0.666 #random scale shrinking factor
    for x in xrange(5): #number of tries before giving up
        print("try: "+str(x+1))
        for i in xrange(np):
            multiplier = scaledp((1/xf, xf))
            if paramState == None or old_params == None:
                pdb.set_trace()
            paramState[i] = multiplier*old_params[i]

        print("randomized parameters")
        print("trying: " + c_arr2str(paramState))

        new_err = runCalc(paramState)

        print("errls", new_err)
        if consistant(new_err):
            print("consistant")
            t_err = sum([x**2 for x in new_err]) / len(new_err)
            t_err = t_err**0.5
            print("terr", t_err)
            if not err or t_err < err:
                print("smaller")
                paramState = recursiveSearch(paramState, xf, t_err)
                if paramState:
                    return paramState
            else:
                print("could not find new param state")
        paramState = old_params

    return None

xf = float(3)
newParamState = lo.pArr(1, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 26000)

# for i in xrange(np):
#     newParamState[i] = scaledp((1/xf, xf))*newParamState[i]
out_params = recursiveSearch(newParamState, xf/0.666, None)

print(c_arr2str(out_params))



# matrix = [[matrix[i][j] for i in xrange(len(matrix))] for j in xrange(len(matrix[0]))]
# matrix = makeSignChanges(matrix)
# calcCorMatrix(matrix, "cor_" + timestr)