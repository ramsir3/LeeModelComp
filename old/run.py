import function
import numpy
import plotly.offline as py
import plotly.graph_objs as go


dt = 0.01
t1 = 1
initialValues = {'MR':[float(0)],'R':[float(0)], 'R2':[float(0)], 'O':[float(1)], 'I':[float(0)], 'I2R2':[float(0)], 'MY':[float(0)], 'Y':[float(0)], 'YIex':[float(0)]}
model = function.LacOperon(initialValues, dt, t1)
time = numpy.arange(0, t1, dt)
data = model.go()
# print(data)
print data

traces = [go.Scatter(x=time, y=data[trace], name=trace) for trace in data.keys()]
# Plot and embed in ipython notebook!
py.plot(traces, filename='basic-line.html', auto_open=False)