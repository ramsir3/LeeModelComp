import plotly.offline as py
import plotly.graph_objs as go

def plot(data, chars, names, smplrt, filename, r):
    ############## EXTRACT ##################
    # smplrt = 1
    numPoints = data.size
    numSpecies = len(chars)
    time = [data.time[j] for j in xrange(0, numPoints, smplrt)]
    vals = [[data.vals[i][j] for j in xrange(0, numPoints, smplrt)] for i in xrange(numSpecies)]
    ################ PLOT ###################
    traces = []
    if not r:
        r = xrange(numSpecies)
    for i in r:
        traces.append(
            go.Scatter(
                x=time,
                y=vals[i],
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

    py.plot(traces, filename='results/'+filename+'.html', auto_open=False)