from ctypes import *

ODE = CFUNCTYPE(POINTER(c_double), POINTER(c_double))

class ModelStruct(Structure):
    _fields_ = [
        ("initValues",POINTER(c_double)),
        ("params", POINTER(c_double)),
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

class ModelEngine(object):
    """docstring for ModelEngine"""
    def __init__(self, mstring):
        super(ModelEngine, self).__init__()
        self.engine = CDLL("./lib/engine.dll")
        self.model = CDLL("./lib/" + mstring + ".dll") #the model dll file

        self.model.getNumSpecies.restype = c_int
        self.model.getNumParams.restype = c_int
        self.model.getNames.restype = POINTER(c_char_p)
        self.nP = self.model.getNumParams()
        self.nS = self.model.getNumSpecies()

        self.pArr = c_double * self.nP
        self.iArr = c_double * self.nS

        self.model.getModel.argtypes = [POINTER(c_double), POINTER(c_double)]
        self.model.getModel.restype = ModelStruct

        self.engine.freeTime.argtypes = [c_void_p]
        self.engine.freeVals.argtypes = [c_void_p, c_int]
        self.engine.go.argtypes = [ModelStruct, c_double, c_double]
        self.engine.go.restype = ResultStructure

    def free(self, data, num):
        self.engine.freeTime(data.time)
        self.engine.freeVals(data.values, num)

    def getSize(self):
        return (self.nP, self.nS)

    def getNames(self):
        return self.model.getNames()

    def go(self, params, initValues, dt, t1):
        return self.engine.go(self.model.getModel(initValues, params), c_double(dt), c_double(t1))



