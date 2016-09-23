from ctypes import *
from lib import *
import plotly.offline as py
import plotly.graph_objs as go

################# SETUP ##################
engine = CDLL("./lib/engine.dll")
model = CDLL("./lib/lacoperon.dll") #the model dll file

model.getNumSpecies.restype = c_int
model.getNumParams.restype = c_int
pArr = c_double * model.getNumParams()
iArr = c_double * model.getNumSpecies()

moxdel.getModel.argtypes = [POINTER(c_double), POINTER(c_double)]
model.getModel.restype = ModelStruct

engine.freeTime.argtypes = [c_void_p]
engine.freeVals.argtypes = [c_void_p, c_int]
engine.go.argtypes = [ModelStruct, c_double, c_double]
engine.go.restype = ResultStructure

################ SET PARAMS #################
dt =  0.0000125
t1 = 80
smplrt = int((t1/dt)/1000)


params = pArr(1, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 25000)

initialVals = iArr(0, 0, 0, 1, 0, 0, 0, 0, 0)

# uncomment below to use model defaults
# params = None
# initialVals = None

################# EXECUTE #####################
m = model.getModel(initialVals, params)
data = engine.go(m, c_double(dt), c_double(t1))

############### EXTRACT ##################
numPoints = data.size
time = [data.time[j] for j in range(0, numPoints, smplrt)]
values = [[data.values[i][j] for j in range(0, numPoints, smplrt)] for i in range(m.numSpecies)]

engine.freeTime(data.time)
engine.freeVals(data.values, model.getNumSpecies())

print time[-1]


################ PLOT ###################
traces = []
r = range(m.numSpecies)
# r = [0,1,2,3,5,6,7,8]
for i in r:
    traces.append(
        go.Scatter(
            x=time,
            y=values[i],
            name=m.names[i]
            )
        )

py.plot(traces, filename='basic-line.html', auto_open=False)