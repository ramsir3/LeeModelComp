# equation(3)
def dMRdt()
    return ksMR-lMR*MR

# equation(4)
def dRdt()
 return ksR*MR-2*k2R*(R**2)+2*kn2R*R2-lR*R

# equation(5)
def dR2dt()
    return k2R*(R**2)-kn2R*R2-kr*R2*O+knr*(OT-O)-kdr1*R2*(I**2)+kndr1*I2R2-lR2*R2

# equation(6)
def dOdt()
    return -kr*R2*O+knr*(OT-O)+kdr2*(OT-O)*(I**2)-kndr2*O*I2R2

# equation(7)
def dIdt()
    return -2*kdr1*R2*(I**2)+2*kndr1*I2R2-2*kdr2*(OT-O)*(I**2)+2*kndr2*O*I2R2+kft*YIex+kt*(Iex-I)+2*lI2R2*I2R2+lYIex*YIex

# equation(8)
def dI2R2dt()
    return kdr1*R2*(I**2)-kndr1*I2R2+kdr2*(OT-O)*(I**2)-kndr2*O*I2R2-lI2R2*I2R2

# equation(9)
def dMYdt()
    return ks0MY*(OT-O)+ks1MY*O-lMY*MY

# equation(10)
def dYdt()
    return ksY*MY+(kft+knp)*YIex-kp*Y*Iex-lY*Y

# equation(11)
def dYIexdt()
    return -(kft+knp)*YIex+kp*Y*Iex-lYIex*YIex