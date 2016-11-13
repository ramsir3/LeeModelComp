from lib import Model, Engine
import datetime
import plotly.offline as py
import plotly.graph_objs as go

################# SETUP ##################
m = Model("lacoperon")
e = Engine()

################ SET PARAMS #################
dt =  0.0000025
t1 = 80
smplrt = int((t1/dt)/1000)


params = m.pArr(1, 0.23, 15, 50, 0.001, 960, 2.4, 0.0000003, 12,
    0.0000003, 4800, 0.5, 0.01, 30, 0.12, 0.1, 60000, 0.92, 0.462, 0.462, 0.2,
    0.2, 0.2, 0.2, 0.2, 25000)

params = m.pArr(0.154977514043, 1.16462169406, 7.03433844184, 154.746207648, 0.00019537219059, 7118.81963368, 24.6690045197, 2.38337847508e-07, 4.11519429287, 1.95971542799e-07, 47383.95692, 0.387249488649, 0.0220698650347, 22.6682218121, 0.00422368688352, 0.958937842327, 13966.6093417, 0.84513174251, 6.1302738193, 3.82796984736, 0.0811790521043, 0.0740019990288, 0.0443714858756, 0.042983581708, 6.00254638463, 37610.8755213)
# params = m.pArr(2.87291065265, 0.209400206678, 7.51636699019, 1180.76712299, 0.000289911945754, 189.53551479, 8.23132491843, 4.27639769966e-07, 2.22698494574, 6.85695326561e-06, 825.049766525, 0.567406272303, 0.0975143681116, 11.7119727273, 0.0396695147201, 1.51547287798, 40385.761299, 17.4839005396, 5.29433419242, 0.955242980096, 0.0406939846717, 0.740798430267, 0.654389301377, 0.404157205932, 0.132430369897, 38981.1412208)
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
timestr = datetime.datetime.now().strftime("%I-%M-%S")
py.plot(traces, filename='results/basic-line_'+timestr+'.html', auto_open=False)