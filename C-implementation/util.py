from math import floor

def extrema(data, size, cross):
    if size <= 2:
        return None
    pre_dt = data[1]-data[0]
    dt = pre_dt
    for i in xrange(2, size):
        if pre_dt != dt:
            print("help")
        dt = data[i] - data[i-1]
        # print(dt)
        zero = lambda x: (x <= 0.000000000000001 and x >= -0.000000000000001)
        # if not zero(dt) and not zero(pre_dt):
        isPeak = cross(pre_dt, dt)
        # if i < int(2.5/0.000005) and i > int(2/0.000005):
        #     print(isPeak, pre_dt, dt)
        if isPeak:
            print(isPeak, pre_dt, dt)
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

def find2HalfsPeak(data, size, cross, partial):
    ind = extrema(data, size, cross)
    print(ind)
    if ind:
        val = (data[ind]+data[0])*partial
        # print(val)
        one = find(data, ind, 0, partial)
        two = find(data, ind, size, partial)
        # print(ind, one, two)
        return (ind, one, two)
    return (None, None, None)


def package(data, time, ind):
    dout = []
    tout = []
    for i in ind:
        dout.append(data[i] if i else None)
        tout.append(time[i] if i else None)
    return (dout, tout)

def c_arr2str(c_arr):
    out = ""
    for i in range(len(c_arr)):
        out += str(c_arr[i])+", "
    return out[:-2]

def sensitivity2str(sr, names):
    ns = len(sr)
    out = ","
    for i in xrange(ns):
        out += names[i]+",,"
    out += "\n,"
    for i in xrange(ns):
        out += "dy,dt,"
    out += "\npeak,"
    for i in xrange(ns):
        out += str(sr[i][0][0]) + "," + str(sr[i][1][0]) + ","
    out += "\nhalf rise,"
    for i in xrange(ns):
        out += str(sr[i][0][1]) + "," + str(sr[i][1][1]) + ","
    out += "\nhalf fall,"
    for i in xrange(ns):
        out += str(sr[i][0][2]) + "," + str(sr[i][1][2]) + ","
    # print(out)
    return out