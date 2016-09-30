from ctypes import *

ODE = CFUNCTYPE(POINTER(c_double), POINTER(c_double))

class ModelStruct(Structure):
    _fields_ = [
        ("initVals",POINTER(c_double)),
        ("params", POINTER(c_double)),
        ("bolus", POINTER(c_double)),
        ("funcs", POINTER(ODE)),
        ("numSpecies", c_int),
        ("numParams", c_int)
        ]

class ResultStructure(Structure):
    _fields_ = [
        ("values", POINTER(POINTER(c_double))),
        ("time", POINTER(c_double)),
        ("size", c_int)
        ]

class Model(object):
    """docstring for Model"""
    def __init__(self, mstring):
        super(Model, self).__init__()
        self.model = CDLL("./lib/" + mstring + ".dll") #the model dll file

        self.model.getNumSpecies.restype = c_int
        self.model.getNumParams.restype = c_int
        self.model.getNames.restype = POINTER(c_char_p)
        self.nP = self.model.getNumParams()
        self.nS = self.model.getNumSpecies()

        self.pArr = c_double * self.nP
        self.iArr = c_double * self.nS
        self.bArr = c_double * self.nS

        self.model.getModel.argtypes = [POINTER(c_double), POINTER(c_double)]
        self.model.getModel.restype = ModelStruct

    def getSize(self):
        return (self.nP, self.nS)

    def getNames(self):
        return self.model.getNames()

    def getModel(self, params, initVals, bolus):
        return self.model.getModel(initVals, params, bolus)

class Engine(object):
    """docstring for Engine"""
    def __init__(self):
        super(Engine, self).__init__()
        self.engine = CDLL("./lib/engine.dll")
        self.engine.freeTime.argtypes = [c_void_p]
        self.engine.freeVals.argtypes = [c_void_p, c_int]
        self.engine.go.argtypes = [ModelStruct, c_double, c_double]
        self.engine.go.restype = ResultStructure

    def free(self, data, num):
        self.engine.freeTime(data.time)
        self.engine.freeVals(data.values, num)

    def go(self, model, dt, t1, bp):
        return self.engine.go(model, c_double(dt), c_double(t1), c_int(bp))

class Sensitivity(Engine):
    """docstring for Sensitivties"""
    def __init__(self, model, defParams, defInitVals, bolus, dt, t1, bp, charFunc):
        super(Sensitivity, self).__init__()
        self.model = model
        self.defParams = defParams
        self.defInitVals = defInitVals
        self.bolus = bolus
        self.charFunc = charFunc
        self.dt = dt
        self.t1 = t1
        self.bp = bp
        self.size = self.model.getSize()
        data = self.go(self.defParams, self.defInitVals)
        self.defChars = self.charFunc(data)
        self.free(data)

    def getSize(self):
        return self.size

    def free(self, data):
        return super(Sensitivity, self).free(data, self.size[1])

    def go(self, params, initVals):
        return super(Sensitivity, self).go(self.model.getModel(params, initVals, self.bolus), self.dt, self.t1, self.bp)

    def calcChars(self, params, initVals):
        if not params:
            params = self.defParams
        if not initVals:
            initVals = self.defInitVals
        data = self.go(params, initVals)
        chars = self.charFunc(data)
        return (data, chars)

    def findDelta(self, chars, defChars):
        out = []
        for i in xrange(self.size[1]):
            out.append(([ai - bi if ai and bi else None for ai, bi in zip(chars[i][0], defVal[i][0])],
                        [ai - bi if ai and bi else None for ai, bi in zip(chars[i][1], defVal[i][1])]))
        print out
        return out

    def calc(self, params, initVals):
        data, chars = self.calcChars(params, initVals)
        self.free(data)
        deltaChars = findDelta(chars, self.defChars)
        deltaParams =  [ai - bi for ai, bi in zip(params, self.defParams)]
        return (deltaParams, deltaChars)
