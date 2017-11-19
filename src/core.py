import math

class Core(object):
    m = 18.0 * 1836
    Z = 10
    N = 9
    
    etat0 = 1.792
    etat1 = 0.4515 
    netat0 = 2.710 
    netat1 = 0.3671 

    netat = netat0 + netat1 * (Z - N - 1)
    etat = etat0 + etat1 * (Z - N -1)

    unit = 27.2114 
    Eb1 = 12.62 / unit 
    Eb2 = 14.75 / unit 
    Eb3 = 18.51 / unit 
    Eb4 = 32.4 / unit 
    Eb5 = 539.7 / unit 

    def Omega(self, r):
        return 1 / (self.netat * (math.exp(r * self.etat) - 1) / self.etat + 1)

    def Zc(self, r):
        return self.Z - self.N * (1 - self.Omega(r))

    def dZc(self, r):
        return - self.N * self.netat * math.exp(r * self.etat) * self.Omega(r) * * 2

    def Vc(self, r):
        return self.Zc(r) / r 

    def find_max_radius(self, Eb, x, y):
        tolerance = 1e-14
        a = x 
        b = y 
        while math.abs(b - a) >= tolerance:
            c = (a + b) / 2
            if (self.Vc(a) - Eb) * (self.Vc(c) - Eb) > 0:
                a = c 
            else:
                b = c 

        c = a 
        return c 

    def generate_radius(Eb):
        pass 

