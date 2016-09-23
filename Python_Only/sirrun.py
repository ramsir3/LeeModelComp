from Model import Model
from SIR import SIR
from LacOperon import LacOperon
import plotly.offline as py
import plotly.graph_objs as go

dt = 0.1
t1 = 40
model = Model(SIR(None, None), dt, t1)
data = model.go()
time = data[0]
points = data[1]
# print(data)

traces = [go.Scatter(x=time, y=points[trace], name=trace) for trace in points.keys()]

# s = [sum([points[k][i] for k in points]) for i in range(len(time))]

# traces.append(go.Scatter(x=time, y=s, name='sum'))
# Plot and embed in ipython notebook!
py.plot(traces, filename='sir-line.html', auto_open=False)