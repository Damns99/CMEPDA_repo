import math

LIGHT_SPEED=1.

class Particle:
    def __init__(self, name, mass, charge, beta=0.):
        self.name = name
        self.mass = mass
        self.charge = charge
        self.beta = beta
    
    def print_info(self):
        print(f'{self.name}: mass = {self.mass:.3f} MeV/c^2   charge = {self.charge} e')
        print(f'beta = {self.beta:.3f} c   gamma = {self.gamma:.3f}')
        print(f'energy = {self.energy:.3f} MeV   momentum = {self.momentum:.3f} MeV/c\n')
    
    @property
    def beta(self):
        return self._beta
    @beta.setter
    def beta(self, newbeta):
        if (newbeta < 0. or newbeta > 1.):
            print(f'Invalid beta {newbeta}, possible values lay between 0. and 1.')
            print('Beta will be set to zero by default.\n')
            self._beta = 0.
        else:
            self._beta = newbeta
    
    @property
    def gamma(self):
        return 1./math.sqrt(1. - self.beta**2)
    @gamma.setter
    def gamma(self, newgamma):
        if (newgamma < 1.):
            print(f'Invalid gamma {newgamma}, possible values are >= 1.\n')
        else:
            self.beta = math.sqrt(1. - 1./newgamma**2)
    
    @property
    def energy(self):
        return self.gamma*self.mass
    @energy.setter
    def energy(self, newenergy):
        if (newenergy < self.mass):
            print(f'Invalid energy {newenergy}, it cannot be lower than the mass {self.mass}\n')
        else:
            self.gamma = newenergy / self.mass
        
    @property
    def momentum(self):
        return self.gamma*self.mass*self.beta
    @momentum.setter
    def momentum(self, newmomentum):
        if (newmomentum < 0.):
            print(f'Invalid momentum {newmomentum}, it cannot be negative\n')
        else:
            self.beta = (newmomentum/self.mass) / math.sqrt(1+(newmomentum/self.mass)**2)
        

class Proton(Particle):
    NAME = 'Proton'
    MASS = 938.272
    CHARGE = +1.

    def __init__(self, beta=0.):
        super().__init__(self.NAME, self.MASS, self.CHARGE, beta)


class Alpha(Particle):
    NAME = 'Alpha'
    MASS = 3727.3
    CHARGE = +4.

    def __init__(self, beta=0.):
        super().__init__(self.NAME, self.MASS, self.CHARGE, beta)

if __name__ == '__main__':
    proton = Proton(200.)
    proton.print_info()
    proton.beta = 0.8
    proton.print_info()
    alpha = Alpha(20.)
    alpha.energy = 10000.
    alpha.print_info()