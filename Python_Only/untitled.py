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
        return out if out >= 0 else 0
    # equation(9):
    def dMYdt(self, last):
        out = (self.params['ks0MY']*(self.params['OT']-last['O']))+(self.params['ks1MY']*last['O'])-(self.params['lMY']*last['MY'])
        return out
    # equation(10):
    def dYdt(self, last):
        out = (self.params['ksY']*last['MY'])+((self.params['kft']+self.params['knp'])*last['YIex'])-(self.params['kp']*last['Y']*self.params['Iex'])-(self.params['lY']*last['Y'])
        return out if out >= 0 else 0
    # equation(11):
    def dYIexdt(self, last):
        out = -((self.params['kft']+self.params['knp'])*last['YIex'])+(self.params['kp']*last['Y']*self.params['Iex'])-(self.params['lYIex']*last['YIex'])
        return out

