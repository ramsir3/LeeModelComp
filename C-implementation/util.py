from math import floor

def extrema(data, size, cross):
    if size <= 2:
        return None
    pre_dt = data[1]-data[0]
    for i in xrange(2, size):
        dt = data[i] - data[i-1]
        # print(dt)
        if dt != 0 and pre_dt != 0:
            if cross(pre_dt, dt):
                return i
        pre_dt = dt
    return None



def find(data, ind1, ind2, partial):
    i = ind1
    thr = abs(data[ind1] - data[0])
    thr = thr - int(thr)
    x = 0
    while floor(thr) == 0:
        thr *= 10
        x += 1
    thr = 10**(-(x if x > 3 else 3))

    val = (data[ind1] + data[0])*partial
    r = xrange(ind1, ind2)
    if ind1 > ind2:
        r = reversed(xrange(ind2, ind1))
    for i in r:
        err = (data[i]-val)/val
        if  abs(err) < thr :
            return i
    return None

def find2HalfsPeak(data, size, partial):
    cross = lambda x,y: x < 0 and y > 0
    ind = extrema(data, size, cross)
    if not ind:
        cross = lambda x,y: x > 0 and y < 0
        ind = extrema(data, size, cross)
    if ind:
        val = (data[ind]+data[0])*partial
        print(val)
        one = find(data, ind, 0, partial)
        two = find(data, ind, size, partial)
        print(ind, one, two)
        return (ind, one, two)
    return (None, None, None)


def package(data, time, ind):
    dout = []
    tout = []
    for i in ind:
        dout.append(data[i] if i else None)
        tout.append(time[i] if i else None)
    return (dout, tout)