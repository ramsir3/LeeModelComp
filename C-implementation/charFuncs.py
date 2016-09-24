from util import *
from LacOperonConsts import *


def sirCharFunc(data):
    vals = data.values
    time = data.time
    size = data.size

    ind = maxima(vals[1], size)
    print(ind)
    return [vals[1][ind], time[ind]]


def lacOpCharFunc(data):
    vals = data.values
    time = data.time
    size = data.size

    ind = maxima(vals[I], size)
    print(ind)
    return [vals[I][ind], time[ind]]



