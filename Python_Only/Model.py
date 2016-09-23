from numpy import arange

class Model():

    def __init__(self, model, dt, t1):
        self.model = model
        self.values = model.values
        self.dt = dt
        self.t1 = t1

    def getLast(self, values):
        out = dict()
        for k in values:
            out[k] = values[k][-1]
        # print out
        return out

    def minZero(self, inpt):
        if inpt >= 0:
            return inpt
        else:
            return 0

    def go(self):
        t = arange(0, self.t1, self.dt)
        # print t
        traces = sorted(self.values.keys())
        # print(self.getLast(self.values))
        for i in t:
            lasts = self.getLast(self.values)
            for key in lasts:
                newVal = lasts[key] + (self.model.funcs[key](lasts)*self.dt)
                self.values[key].append(newVal)
        return (t, self.values)
