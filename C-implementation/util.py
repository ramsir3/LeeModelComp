def maxima(vals, size):
    if size <= 2:
        return None
    done = False
    prevSign = vals[1]-vals[0] > 0
    i = 2
    while not done:
        if i >= size:
            return None
        sign = vals[i] - vals[i-1] > 0
        # print(i)
        if not sign and prevSign:
            return i
        i += 1
    return None

def alternate(vals, time, ind):
    out = []
    for i in ind:
        out.append(vals[i])
        out.append(time[i])
    return out