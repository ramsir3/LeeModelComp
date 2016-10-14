from scipy.stats.stats import pearsonr
import charmatrix as cm
import numpy as np
import matplotlib.pyplot as plt
from heatmapcluster import heatmapcluster

m = cm.matrix

cor = [[0 for x in xrange(len(m))] for y in xrange(len(m))]

for i in xrange(len(m)):
    for j in xrange(len(m)):
        if m[i][0] != None and m[j][0] != None:
            cor[i][j] = pearsonr(m[i], m[j])[0]
        else:
            cor[i][j] = None
fn = "cor.csv"
f = open(fn, 'w')

strcor = str(cor)[1:-1].replace("], ", "\n").replace("[","").replace("]", "")

f.write(strcor)
f.close()

sp = ["MR", "R", "R2", "O", "I", "I2R2", "MY", "Y", "YIex"]
ch = ["dPK", "dPKT", "dHRT", "dHFT"]

names = list()
for x in xrange(len(sp)):
    for y in xrange(len(ch)):
        names.append(sp[x] + ' ' + ch[y])
names.remove("MR dPKT")
names.remove("MR dHRT")
names = list(reversed(names))

data = np.genfromtxt(fn, delimiter=",")


clustersize = 12
h = heatmapcluster(data, names, names,
                   num_row_clusters=clustersize, num_col_clusters=clustersize,
                   label_fontsize=9,
                   xlabel_rotation=-75,
                   cmap=plt.cm.coolwarm,
                   show_colorbar=True,
                   top_dendrogram=True)
plt.savefig("cor_heatmap.png")