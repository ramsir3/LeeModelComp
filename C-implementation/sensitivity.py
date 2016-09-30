from LacOperon import *
from SIR import *
from lib import Engine
import plotly.offline as py
import plotly.graph_objs as go
import datetime

# sir = SIR()

# dt = 0.01
# t1 = 100

# defParams =  sir.pArr(0.5, 0.333)
# defInitialVals = None

# newParams = sir.pArr(0.75, 0.333)

# s = Sensitivities(sir, defParams, defInitialVals, dt, t1, sirCharFunc)
# out = s.calcSensitivity(newParams, None)
# print out

lo = LacOperon()

dt =  0.0000125
t1 = 50
bp = int(5/0.0000125)
smplrt = int((t1/dt)/100000)

defParams = lo.pArr(1, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 25000)

defInitialVals = lo.iArr(0.4978354978306917, 0.27228876937802426, 0.5213396786687533, 0.004850296769185558, 37479.45847464454, 18.011347105968394, 0.026789275794458223, 3.827040310495846, 0.19135105876949846)

# bolus = None
bolus = lo.bArr(0, 0, 0, 0, 100000, 0, 0, 0, 0)

e = Engine()
lom = lo.getModel(defParams, defInitialVals, None)
data = e.go(lom, dt, t1, -1)

ssVals = [data.values[i][data.size - 1] for i in xrange(lo.getSize()[1])]
e.free(data, 9)
print("SS:", ssVals)
ssVals = lo.iArr(ssVals[0], ssVals[1], ssVals[2], ssVals[3], ssVals[4], ssVals[5], ssVals[6], ssVals[7], ssVals[8])

newParams = lo.pArr(2, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 25000)

t1 = 50
s = Sensitivity(lo, defParams, ssVals, bolus, dt, t1, bp, lacOpCharFunc)
out = s.calcChars(None, None)

# lom = lo.getModel(defParams, ssVals, bolus)
# data = e.go(lom, dt, t1, bp)

data = out[0]
chars = out[1]
smplrt = int((t1/dt)/1000)
numPoints = data.size
print(chars)
############## EXTRACT ##################
numSpecies = lo.getSize()[1]
numPoints = data.size
names = lo.getNames()
time = [data.time[j] for j in xrange(0, numPoints, smplrt)]
values = [[data.values[i][j] for j in xrange(0, numPoints, smplrt)] for i in xrange(numSpecies)]

s.free(data)

################ PLOT ###################
traces = []
r = [1,2]
r = xrange(numSpecies)
for i in r:
    traces.append(
        go.Scatter(
            x=time,
            y=values[i],
            name=names[i]
            )
        )

for i in r:
    traces.append(
        go.Scatter(
            x=chars[i][1],
            y=chars[i][0],
            mode = 'markers',
            name=names[i] + ' chars'
            )
        )

py.plot(traces, filename='results/'+datetime.datetime.now().strftime("%I-%M-%S")+'.html', auto_open=False)

# print out