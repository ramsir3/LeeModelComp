class LacOperon():
    """docstring for SIR"""
    params = {
    'OT': 1,
    'ksMR': 0.23,
    'ksR': 15,
    'k2R': 50,
    'kn2R': 10**-3,
    'kr': 960,
    'knr': 2.4,
    'kdr1': 3*(10**-7),
    'kndr1': 12,
    'kdr2': 3*(10**-7),
    'kndr2': 4.8*(10**3),
    'ks1MY': 0.5,
    'ks0MY': 0.01,
    'ksY': 30,
    'kp': 0.12,
    'knp': 0.1,
    'kft': 6*(10**4),
    'kt': 0.92,
    'lMR': 0.462,
    'lMY': 0.462,
    'lR': 0.2,
    'lR2': 0.2,
    'lY': 0.2,
    'lYIex': 0.2,
    'lI2R2': 0.2,
    'Iex': 25
    }

    values = {
    'MR':[0],
    'R':[0],
    'R2':[0],
    'O':[1],
    'I':[0],
    'I2R2':[0],
    'MY':[0],
    'Y':[0],
    'YIex':[0]
    }

    def __init__(self, params, values):
        self.funcs = {
        'MR':self.dMRdt,
        'R':self.dRdt,
        'R2':self.dR2dt,
        'O':self.dOdt,
        'I':self.dIdt,
        'I2R2':self.dI2R2dt,
        'MY':self.dMYdt,
        'Y':self.dYdt,
        'YIex':self.dYIexdt
        }

        if params:
            self.params = params

        if values:
            self.values = values

    # equation(3):
    def dMRdt(self, last):
        out = self.params['ksMR']-(self.params['lMR']*last['MR'])
        return out
    # equation(4):
    def dRdt(self, last):
        out = (self.params['ksR']*last['MR'])-(2*self.params['k2R']*(last['R']**2))+(2*self.params['kn2R']*last['R2'])-(self.params['lR']*last['R'])
        return out
    # equation(5):
    def dR2dt(self, last):
        # print(last)
        out = (self.params['k2R']*(last['R']**2))-(self.params['kn2R']*last['R2'])-(self.params['kr']*last['R2']*last['O'])+(self.params['knr']*(self.params['OT']-last['O']))-(self.params['kdr1']*last['R2']*(last['I']**2))+(self.params['kndr1']*last['I2R2'])-(self.params['lR2']*last['R2'])
        return out
    # equation(6):
    def dOdt(self, last):
        out = -(self.params['kr']*last['R2']*last['O'])+(self.params['knr']*(self.params['OT']-last['O']))+(self.params['kdr2']*(self.params['OT']-last['O'])*(last['I']**2))-(self.params['kndr2']*last['O']*last['I2R2'])
        return out
    # equation(7):
    def dIdt(self, last):
        out = -(2*self.params['kdr1']*last['R2']*(last['I']**2))+(2*self.params['kndr1']*last['I2R2'])-(2*self.params['kdr2']*(self.params['OT']-last['O'])*(last['I']**2))+(2*self.params['kndr2']*last['O']*last['I2R2'])+(self.params['kft']*last['YIex'])+(self.params['kt']*(self.params['Iex']-last['I']))+(2*self.params['lI2R2']*last['I2R2'])+(self.params['lYIex']*last['YIex'])
        return out
    # equation(8):
    def dI2R2dt(self, last):
        out = (self.params['kdr1']*last['R2']*(last['I']**2))-(self.params['kndr1']*last['I2R2'])+(self.params['kdr2']*(self.params['OT']-last['O'])*(last['I']**2))-(self.params['kndr2']*last['O']*last['I2R2'])-(self.params['lI2R2']*last['I2R2'])
        return out
    # equation(9):
    def dMYdt(self, last):
        out = (self.params['ks0MY']*(self.params['OT']-last['O']))+(self.params['ks1MY']*last['O'])-(self.params['lMY']*last['MY'])
        return out
    # equation(10):
    def dYdt(self, last):
        out = (self.params['ksY']*last['MY'])+((self.params['kft']+self.params['knp'])*last['YIex'])-(self.params['kp']*last['Y']*self.params['Iex'])-(self.params['lY']*last['Y'])
        return out
    # equation(11):
    def dYIexdt(self, last):
        out = -((self.params['kft']+self.params['knp'])*last['YIex'])+(self.params['kp']*last['Y']*self.params['Iex'])-(self.params['lYIex']*last['YIex'])
        return out


