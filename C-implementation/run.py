from lib import Model, Engine
import plotly.offline as py
import plotly.graph_objs as go

################# SETUP ##################
m = Model("lacoperon")
e = Engine()

################ SET PARAMS #################
dt =  0.0000125
t1 = 80
smplrt = int((t1/dt)/1000)


params = m.pArr(1, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 25000)

initialVals = m.iArr(0, 0, 0, 1, 0, 0, 0, 0, 0)

# uncomment below to use model defaults
# params = None
# initialVals = None

################# EXECUTE #####################
lo = m.getModel(params, initialVals, None)
data = e.go(lo, dt, t1, -1)
# print("data", type(data))

############### EXTRACT ##################
numSpecies = m.getSize()[1]
numPoints = data.size
names = m.getNames()
time = [data.time[j] for j in xrange(0, numPoints, smplrt)]
vals = [[data.vals[i][j] for j in xrange(0, numPoints, smplrt)] for i in xrange(numSpecies)]

e.free(data, numSpecies)
print time[-1]


################ PLOT ###################
traces = []
r = xrange(numSpecies)
# r = [0,1,2,3,5,6,7,8]
for i in r:
    traces.append(
        go.Scatter(
            x=time,
            y=vals[i],
            name=names[i]
            )
        )

py.plot(traces, filename='basic-line.html', auto_open=False)