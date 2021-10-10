''' assegnamento_3.py:
    Create a ProbabilityDensityFunction class that is capable of throwing
    pseudo-random number with an arbitrary distribution.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import random

class ProbabilityDensityFunction:
    
    def __init__(self, x, y, k = 3):
        self._x = x
        self._y = y
        self._spline = interpolate.UnivariateSpline(x, y, k = k)
        tempx = np.linspace(x[0], x[-1], 1000)
        tempy = np.array([self.prob_interval(x[0], tx) for tx in tempx])
        tempx, tempy = np.transpose(np.array([[item[0], item[1]] for item in zip(tempx, tempy, np.append(1, np.diff(tempy))) if item[2] != 0]))
        self._ppf = interpolate.UnivariateSpline(tempy, tempx, k = k)
    
    def __call__(self, newx):
        return self._spline(newx)
    
    def prob_interval(self, x0, x1):
        return self._spline.integral(x0, x1) / self._spline.integral(self._x[0], self._x[-1])
    
    def ppf(self, x):
        return self._ppf(x)
    
    def random(self):
        randx = random.random()
        return self._ppf(randx)

def myfun(x):
    return np.logical_and(x >= 0, x < 1)

def myfun2(x):
    return 10*x*(x >= 0)*(x < 0.1) + 1*(x >= 0.1)*(x < 0.9) + 10*(1-x)*(x >= 0.9)*(x < 1)

plt.figure(1)
plt.grid()

samplex = np.linspace(0, 1, 100)
sampley = myfun2(samplex)
mypdf = ProbabilityDensityFunction(samplex, sampley, k = 5)

newx = np.linspace(0, 1, 1000)

plt.plot(samplex, sampley, 'r.')
plt.plot(newx, mypdf(newx), 'g.')
plt.plot(newx, mypdf.ppf(newx), 'b.')

plt.figure(1)
plt.grid()

N = 1000000
Nbins = 10000
randx = np.array([mypdf.random() for i in range(N)])

plt.hist(randx, Nbins, range = [0, 1], density = True)

plt.show()