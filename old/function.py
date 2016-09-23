import math
import numpy

class LacOperon:
    initalValues = []
    dt = 0.01
    t1 = 10
    OT = 1
    ksMR = float(0.23)
    ksR = float(15)
    k2R = float(50)
    kn2R = float(10**-3)
    kr = float(960)
    knr = float(2.4)
    kdr1 = float(3*(10**-7))
    kndr1 = float(12)
    kdr2 = float(3*(10**-7))
    kndr2 = float(4.8*(10**3))
    ks1MY = float(0.5)
    ks0MY = float(0.01)
    ksY = float(30)
    kp = float(0.12)
    knp = float(0.1)
    kft = float(6*(10**4))
    kt = float(0.92)
    lMR = float(0.462)
    lMY = float(0.462)
    lR = float(0.2)
    lR2 = float(0.2)
    lY = float(0.2)
    lYIex = float(0.2)
    lI2R2 = float(0.2)
    Iex = float(25000)

    # [MR, R, R2, O, I, I2R2, MY, Y, YIex] = s0
    def __init__(self, initalValues, dt, t1):
        self.initalValues = initalValues
        self.dt = dt
        self.t1 = t1
        self.ft = {'MR':self.dMRdt,'R':self.dRdt, 'R2':self.dR2dt, 'O':self.dOdt, 'I':self.dIdt, 'I2R2':self.dI2R2dt, 'MY':self.dMYdt, 'Y':self.dYdt, 'YIex':self.dYIexdt}

    def setParams(params):
        self.OT = params[0]
        self.ksMR = params[1]
        self.ksR = params[2]
        self.k2R = params[3]
        self.kn2R = params[4]
        self.kr = params[5]
        self.knr = params[6]
        self.kdr1 = params[7]
        self.kndr1 = params[8]
        self.kdr2 = params[9]
        self.kndr2 = params[10]
        self.ks1MY = params[11]
        self.ks0MY = params[12]
        self.ksY = params[13]
        self.kp = params[14]
        self.knp = params[15]
        self.kft = params[16]
        self.kt = params[17]
        self.lMR = params[18]
        self.lMY = params[19]
        self.lR = params[20]
        self.lR2 = params[21]
        self.lY = params[22]
        self.lYIex = params[23]
        self.lI2R2 = params[24]
        self.Iex = params[25]

    def go(self):
        t = numpy.arange(0, self.t1, self.dt)
        traces = sorted(self.initalValues.keys())
        # print(self.getLast(self.initalValues))
        for i in t:
            lasts = self.getLast(self.initalValues)
            for key in self.initalValues:
                newVal = self.initalValues[key][-1] + self.ft[key](lasts)*self.dt
                self.initalValues[key].append(newVal)
        return self.initalValues

    def minZero(self, inpt):
        if not math.isnan(inpt) and inpt >= 0:
            return inpt
        else:
            return 0

    def getLast(self, inpt):
        names = ['MR','R', 'R2', 'O', 'I', 'I2R2', 'MY', 'Y', 'YIex']
        return [self.initalValues[names[i]][-1] for i in range(len(names))]

    # equation(3):
    def dMRdt(self, s0):
        MR, R, R2, O, I, I2R2, MY, Y, YIex = s0
        out = self.ksMR-(self.lMR*MR)
        return out
    # equation(4):
    def dRdt(self, s0):
        MR, R, R2, O, I, I2R2, MY, Y, YIex = s0
        out = (self.ksR*MR)-(2*self.k2R*(R**2))+(2*self.kn2R*R2)-(self.lR*R)
        return out
    # equation(5):
    def dR2dt(self, s0):
        MR, R, R2, O, I, I2R2, MY, Y, YIex = s0
        # print(s0)
        out = (self.k2R*(R**2))-(self.kn2R*R2)-(self.kr*R2*O)+(self.knr*(self.OT-O))-(self.kdr1*R2*(I**2))+(self.kndr1*I2R2)-(self.lR2*R2)
        return out
    # equation(6):
    def dOdt(self, s0):
        MR, R, R2, O, I, I2R2, MY, Y, YIex = s0
        out = -(self.kr*R2*O)+(self.knr*(self.OT-O))+(self.kdr2*(self.OT-O)*(I**2))-(self.kndr2*O*I2R2)
        return out
    # equation(7):
    def dIdt(self, s0):
        MR, R, R2, O, I, I2R2, MY, Y, YIex = s0
        out = -(2*self.kdr1*R2*(I**2))+(2*self.kndr1*I2R2)-(2*self.kdr2*(self.OT-O)*(I**2))+(2*self.kndr2*O*I2R2)+(self.kft*YIex)+(self.kt*(self.Iex-I))+(2*self.lI2R2*I2R2)+(self.lYIex*YIex)
        return out
    # equation(8):
    def dI2R2dt(self, s0):
        MR, R, R2, O, I, I2R2, MY, Y, YIex = s0
        out = (self.kdr1*R2*(I**2))-(self.kndr1*I2R2)+(self.kdr2*(self.OT-O)*(I**2))-(self.kndr2*O*I2R2)-(self.lI2R2*I2R2)
        return out if out >= 0 else 0
    # equation(9):
    def dMYdt(self, s0):
        MR, R, R2, O, I, I2R2, MY, Y, YIex = s0
        out = (self.ks0MY*(self.OT-O))+(self.ks1MY*O)-(self.lMY*MY)
        return out
    # equation(10):
    def dYdt(self, s0):
        MR, R, R2, O, I, I2R2, MY, Y, YIex = s0
        out = (self.ksY*MY)+((self.kft+self.knp)*YIex)-(self.kp*Y*self.Iex)-(self.lY*Y)
        return out if out >= 0 else 0
    # equation(11):
    def dYIexdt(self, s0):
        MR, R, R2, O, I, I2R2, MY, Y, YIex = s0
        out = -((self.kft+self.knp)*YIex)+(self.kp*Y*self.Iex)-(self.lYIex*YIex)
        return out