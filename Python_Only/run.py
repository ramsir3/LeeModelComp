from Model import Model
from SIR import SIR
from LacOperon import LacOperon
import plotly.offline as py
import plotly.graph_objs as go

dt = 0.000025
t1 = 20
# sir = SIR()
def everyNth(l, n, length):
    out = []
    for i in range(length):
        if i % n == 0:
            out.append(l[i])
    return out
smplrt = 100
model = Model(LacOperon(None, None), dt, t1)
data = model.go()
time = data[0]
points = data[1]
numPoints = len(time)

time = everyNth(time, smplrt, numPoints)

# print(data)

traces = [go.Scatter(x=time, y=everyNth(points[trace], smplrt, numPoints), name=trace) for trace in points.keys()]

# s = [sum([points[k][i] for k in points]) for i in range(len(time))]

# traces.append(go.Scatter(x=time, y=s, name='sum'))
# Plot and embed in ipython notebook!
py.plot(traces, filename='basic-line.html', auto_open=False)