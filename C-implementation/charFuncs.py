def nullCharFunc(data):
    vals = data.values
    time = data.time
    size = data.size

    return [vals[1][size//2], time[size//2]]


