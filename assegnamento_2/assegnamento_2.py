''' assegnamento_2.py:
    class Particle with only one between beta, gamma, energy or momentum stored.
    subclasses Proton and Alpha with fixed mass and charge
'''

import math

LIGHT_SPEED=1.

class Particle:
    ''' memorizes name, mass, charge and beta of a particle but has
        energy, gamma and momentum properties equally utilizable
    '''
    def __init__(self, name, mass, charge, beta=0.):
        self.name = name
        self.mass = mass
        self.charge = charge
        self.beta = beta

    def print_info(self):
        ''' prints all particle info in a nice way
        '''
        print(f'{self.name}: mass = {self.mass:.3f} MeV/c^2   charge = {self.charge} e')
        print(f'beta = {self.beta:.3f} c   gamma = {self.gamma:.3f}')
        print(f'energy = {self.energy:.3f} MeV   momentum = {self.momentum:.3f} MeV/c\n')

    @property
    def beta(self):
        ''' particle's beta = velocity / light_speed
        '''
        return self._beta
    @beta.setter
    def beta(self, newbeta):
        if newbeta < 0. or newbeta > 1.:
            print(f'Invalid beta {newbeta}, possible values lay between 0. and 1.')
            print('Beta will be set to zero by default.\n')
            self._beta = 0.
        else:
            self._beta = newbeta

    @property
    def gamma(self):
        ''' particle's gamma = 1 / sqrt(1 - beta**2)
        '''
        return 1./math.sqrt(1. - self.beta**2)
    @gamma.setter
    def gamma(self, newgamma):
        if newgamma < 1.:
            print(f'Invalid gamma {newgamma}, possible values are >= 1.\n')
        else:
            self.beta = math.sqrt(1. - 1./newgamma**2)

    @property
    def energy(self):
        ''' particle's energy = gamma * mass
        '''
        return self.gamma*self.mass
    @energy.setter
    def energy(self, newenergy):
        if newenergy < self.mass:
            print(f'Invalid energy {newenergy}, it cannot be lower than the mass {self.mass}\n')
        else:
            self.gamma = newenergy / self.mass

    @property
    def momentum(self):
        ''' particle's momentum = gamma * mass * beta
        '''
        return self.gamma*self.mass*self.beta
    @momentum.setter
    def momentum(self, newmomentum):
        if newmomentum < 0.:
            print(f'Invalid momentum {newmomentum}, it cannot be negative\n')
        else:
            self.beta = (newmomentum/self.mass) / math.sqrt(1+(newmomentum/self.mass)**2)


class Proton(Particle):
    ''' specification of class Particle for a Proton particle
    '''
    NAME = 'Proton'
    MASS = 938.272
    CHARGE = +1.

    def __init__(self, beta=0.):
        super().__init__(self.NAME, self.MASS, self.CHARGE, beta)


class Alpha(Particle):
    ''' specificaton of class Particle for an Alpha particle
    '''
    NAME = 'Alpha'
    MASS = 3727.3
    CHARGE = +4.

    def __init__(self, beta=0.):
        super().__init__(self.NAME, self.MASS, self.CHARGE, beta)

proton = Proton(200.)
proton.print_info()
proton.beta = 0.8
proton.print_info()
alpha = Alpha(20.)
alpha.energy = 10000.
alpha.print_info()
