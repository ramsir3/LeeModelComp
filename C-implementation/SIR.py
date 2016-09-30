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

def sirCharFunc(data):
    vals = data.values
    time = data.time
    size = data.size

    ind = maxima(vals[1], size)
    return [vals[1][ind], time[ind]]

class SIR(Model):
    """docstring for SIR"""
    def __init__(self):
        super(SIR, self).__init__("sir")

class SIRSensitivity(Sensitivity):
    """docstring for Sensitivties"""
    def __init__(self, defParams, defInitVals, bolus, dt, t1, bp, charFunc):
        super(SIRSensitivities, self).__init__(SIR(), defParams, defInitVals, bolus, dt, bp, t1, charFunc)