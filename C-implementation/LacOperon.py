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

def lacOpCharFunc(data):
    partial = 0.5
    vals = data.values
    time = data.time
    size = data.size

    out = []
    for x in xrange(9):
        out.append(package(vals[x], time, find2HalfsPeak(vals[x], size, partial)))
    return out

class LacOperon(Model):
    """docstring for LacOperon"""
    def __init__(self):
        super(LacOperon, self).__init__("lacoperon")

class LacOperonSensitivity(Sensitivity):
    """docstring for Sensitivties"""
    def __init__(self, defParams, defInitVals, bolus, dt, t1, bp):
        super(LacOpSensitivities, self).__init__(LacOperon(), defParams, defInitVals, bolus, dt, t1, bp, lacOpCharFunc)