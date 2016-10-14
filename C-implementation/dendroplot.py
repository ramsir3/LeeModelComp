import plotly.offline as py
from plotly.graph_objs import *
from plotly.tools import FigureFactory as FF

import numpy as np
from scipy.spatial.distance import pdist, squareform

# get data
# data = np.genfromtxt("http://files.figshare.com/2133304/ExpRawData_E_TABM_84_A_AFFY_44.tab",
#                      names=True,usecols=tuple(range(1,30)),dtype=float, delimiter="\t")
# data_array = data.view((np.float, len(data.dtype.names)))
# data_array = data_array.transpose()
# labels = data.dtype.names

# print(type(data_array), data_array)
# print(type(labels), labels)
def dendroplot(fn, labels):

  data_array = np.genfromtxt(fn, delimiter=",")

  # Initialize figure by creating upper dendrogram
  figure = FF.create_dendrogram(data_array, orientation='bottom', labels=labels)
  for i in range(len(figure['data'])):
      figure['data'][i]['yaxis'] = 'y2'

  # Create Side Dendrogram
  dendro_side = FF.create_dendrogram(data_array, orientation='right')
  for i in range(len(dendro_side['data'])):
      dendro_side['data'][i]['xaxis'] = 'x2'

  # Add Side Dendrogram Data to Figure
  figure['data'].extend(dendro_side['data'])

  # Create Heatmap
  dendro_leaves = dendro_side['layout']['yaxis']['ticktext']
  dendro_leaves = list(map(int, dendro_leaves))
  data_dist = pdist(data_array)
  heat_data = squareform(data_dist)
  heat_data = heat_data[dendro_leaves,:]
  heat_data = heat_data[:,dendro_leaves]

  heatmap = Data([
      Heatmap(
          x = dendro_leaves,
          y = dendro_leaves,
          z = heat_data,
          colorscale = 'YIGnBu'
      )
  ])

  heatmap[0]['x'] = figure['layout']['xaxis']['tickvals']
  heatmap[0]['y'] = dendro_side['layout']['yaxis']['tickvals']

  # Add Heatmap Data to Figure
  figure['data'].extend(Data(heatmap))

  # Edit Layout
  figure['layout'].update({'width':800, 'height':800,
                           'showlegend':False, 'hovermode': 'closest',
                           })
  # Edit xaxis
  figure['layout']['xaxis'].update({'domain': [.15, 1],
                                    'mirror': False,
                                    'showgrid': False,
                                    'showline': False,
                                    'zeroline': False,
                                    'ticks':""})
  # Edit xaxis2
  figure['layout'].update({'xaxis2': {'domain': [0, .15],
                                     'mirror': False,
                                     'showgrid': False,
                                     'showline': False,
                                     'zeroline': False,
                                     'showticklabels': False,
                                     'ticks':""}})

  # Edit yaxis
  figure['layout']['yaxis'].update({'domain': [0, .85],
                                    'mirror': False,
                                    'showgrid': False,
                                    'showline': False,
                                    'zeroline': False,
                                    'showticklabels': False,
                                    'ticks': ""})
  # Edit yaxis2
  figure['layout'].update({'yaxis2':{'domain':[.825, .975],
                                     'mirror': False,
                                     'showgrid': False,
                                     'showline': False,
                                     'zeroline': False,
                                     'showticklabels': False,
                                     'ticks':""}})

  # Plot!
  py.plot(figure, filename='dendrogram_with_heatmap.html', auto_open=False)
