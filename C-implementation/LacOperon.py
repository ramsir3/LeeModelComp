from lib import *
from util import *
#indices
MR = 0
R = 1
R2 = 2
O = 3
I = 4
I2R2 = 5
MY = 6
Y = 7
YIex = 8

hmlabels = ['MR dPK', 'MR dHFT', 'R dPK', 'R dPKT', 'R dHRT', 'R dHFT', 'R2 dPK', 'R2 dPKT', 'R2 dHRT', 'R2 dHFT', 'O dPK', 'O dPKT', 'O dHRT', 'O dHFT', 'I dPK', 'I dPKT', 'I dHRT', 'I dHFT', 'I2R2 dPK', 'I2R2 dPKT', 'I2R2 dHRT', 'I2R2 dHFT', 'MY dPK', 'MY dPKT', 'MY dHRT', 'MY dHFT', 'Y dPK', 'Y dPKT', 'Y dHRT', 'Y dHFT', 'YIex dPK', 'YIex dPKT', 'YIex dHRT', 'YIex dHFT']


param_names = ["OT","ksMR","ksR","k2R","kn2R","kr","knr","kdr1","kndr1","kdr2",
"kndr2","ks1MY","ks0MY","ksY","kp","knp","kft","kt","lMR","lMY",
"lR","lR2","lY","lYIex","lI2R2","Iex"]

def makeSensitivityList(se):
    onePls = list()
    for i in xrange(len(se)):
        seSp = se[i]
        if i == MR:
            onePls += [seSp[0][0]] + [seSp[1][2]]
        else:
            onePls += [seSp[0][0]] + seSp[1]
    return onePls

def makeSignChanges(matrix):
    matrix[6] = [-1*x for x in matrix[6]]
    return matrix


def lacOpCharFunc(data, boluspoint):
    startind = boluspoint - 1
    partial = 0.5
    vals = data.vals
    time = data.time
    size = data.size

    mx = lambda p,n: p > 0 and n < 0
    mn = lambda p,n: p < 0 and n > 0

    out = []
    for x in xrange(9):
        if x in [I, Y, YIex, MY, O]:
            # print("ind:",x)
            out.append(package(vals[x], time, find2HalfsPeak(vals[x], size, mn, startind, partial)))
        else:
            out.append(package(vals[x], time, find2HalfsPeak(vals[x], size, mx, startind, partial)))
    return out

class LacOperon(Model):
    """docstring for LacOperon"""
    def __init__(self):
        super(LacOperon, self).__init__("lacoperon")
        self.charFunc = lacOpCharFunc