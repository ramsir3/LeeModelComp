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
        ("vals", POINTER(POINTER(c_double))),
        ("time", POINTER(c_double)),
        ("size", c_int)
        ]

class Model(object):
    """docstring for Model"""
    def __init__(self, mstring):
        super(Model, self).__init__()
        self.model = CDLL("./lib/" + mstring + ".so") #the model dll file

        self.model.getNumSpecies.restype = c_int
        self.model.getNumParams.restype = c_int
        self.model.getNames.restype = POINTER(c_char_p)
        self.nP = self.model.getNumParams()
        self.nS = self.model.getNumSpecies()

        # print("Model", self.nP)

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
        # if params:
        #     params = (self.pArr)(*params)
        # if initVals:
        #     initVals = (self.iArr)(*initVals)
        # if bolus:
        #     bolus = (self.bArr)(*bolus)

        # c_params = self.move(c_params, params)
        # c_initVals = self.move(c_initVals, initVals)
        # c_bolus = self.move(c_bolus, bolus)

        # print(c_bolus)
        # if bolus:
        #     for x in xrange(len(bolus)):
        #         print(c_bolus[x])
        # for x in xrange(self.nP):
        #     print(x, params[x])
        # for x in xrange(self.nS):
        #     print(bolus[x])
        # for x in xrange(self.nS):
        #     print(bolus[x])

        return self.model.getModel(initVals, params, bolus)

class Engine(object):
    """docstring for Engine"""
    def __init__(self):
        super(Engine, self).__init__()
        self.engine = CDLL("./lib/engine.dll")
        self.engine.freeArr.argtypes = [c_void_p]
        self.engine.freeVals.argtypes = [c_void_p, c_int]
        self.engine.go.argtypes = [ModelStruct, c_double, c_double]
        self.engine.go.restype = ResultStructure
        self.engine.calcSS.argtypes = [ModelStruct, c_double]
        self.engine.calcSS.restype = POINTER(c_double)

    def free(self, data, num):
        self.engine.freeArr(data.time)
        self.engine.freeVals(data.vals, num)

    def freeArr(self, arr):
        self.engine.freeArr(arr)

    def calcSS(self, model, dt):
        return self.engine.calcSS(model, c_double(dt))

    def go(self, model, dt, t1, bp):
        print("entering c land")
        return self.engine.go(model, c_double(dt), c_double(t1), c_int(bp))

class Sensitivity(Engine):
    """docstring for Sensitivties"""
    def __init__(self, dt, t1, bp, charFunc):
        super(Sensitivity, self).__init__()
        self.charFunc = charFunc
        self.dt = dt
        self.t1 = t1
        self.bp = int(bp/dt)
        # data = self.go(self.defModel)
        # self.defChars = self.charFunc(data)
        # self.free(data)

    def calcSS(self, model):
        # print(model.params)
        # for x in xrange(26):
        #     print("p", x, model.params[x])
        return super(Sensitivity, self).calcSS(model, self.dt)

    def go(self, model):
        out = super(Sensitivity, self).go(model, self.dt, self.t1, self.bp)
        return out

    def calcChars(self, model):
        data = self.go(model)
        print("calcing chars")
        chars = self.charFunc(data, self.bp)
        return (data, chars)

    def deltaChars(self, chars, defChars):
        deltaChars = []
        for i in xrange(len(chars)):
            deltaChars.append(([(ai - bi)/bi if ai and bi else None for ai, bi in zip(chars[i][0], defChars[i][0])],
                               [(ai - bi)/bi if ai and bi else None for ai, bi in zip(chars[i][1], defChars[i][1])]))
        return deltaChars

    def deltaParams(self, params, defParams):
        deltaParams =  [ai - bi for ai, bi in zip(params, self.defParams)]
        return deltaParams
