class SIR():
    """docstring for SIR"""
    params = {
    'b':0.5,
    'k':0.3333,
    }

    values = {
    'S': [0.9],
    'I': [0.1],
    'R': [0]
    }

    def __init__(self, params, values):
        self.funcs = {
        'S': self.dSdt,
        'I': self.dIdt,
        'R': self.dRdt
        }

        if params:
            self.params = params

        if values:
            self.values = values

    def dSdt(self, last):
        return -1*self.params['b']*last['S']*last['I']

    def dIdt(self, last):
        return (self.params['b']*last['S']*last['I'])-(self.params['k']*last['I'])

    def dRdt(self, last):
        return self.params['k']*last['I']
