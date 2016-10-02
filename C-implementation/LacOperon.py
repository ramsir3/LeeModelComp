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
    vals = data.vals
    time = data.time
    size = data.size

    mx = lambda p,n: p > 0 and n < 0
    mn = lambda p,n: p < 0 and n > 0

    out = []
    for x in xrange(9):
        if x in [1,2]:
            out.append(package(vals[x], time, find2HalfsPeak(vals[x], size, mn, partial)))
        else:
            out.append(package(vals[x], time, find2HalfsPeak(vals[x], size, mx, partial)))
    return out

class LacOperon(Model):
    """docstring for LacOperon"""
    def __init__(self):
        super(LacOperon, self).__init__("lacoperon")
        self.charFunc = lacOpCharFunc