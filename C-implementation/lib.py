from ctypes import *

ODE = CFUNCTYPE(POINTER(c_double), POINTER(c_double))

class ModelStruct(Structure):
    _fields_ = [
        ("names", POINTER(c_char_p)),
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