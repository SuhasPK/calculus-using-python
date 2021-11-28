# TO FIND CRITICAL POINTS OF A GIVEN FUNCTION - SUMBOLIC METHOD

# LIBRARIES
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

x = sym.symbols('x')
fx = x**2 * sym.exp(-x**2)
dfx = sym.diff(fx)

crit_pnts = sym.solve(dfx)

xx = np.linspace(-4,4,1001)
fxx = sym.lambdify(x,fx)(xx)
dfxx = sym.lambdify(x,dfx)(xx)

print('critical points are ' + str(crit_pnts))

# EXERCISE : PLOT THE CRITICAL POINTS ON THE GIVEN FUNCTION CURVE. 

plt.plot(xx,fxx,label='f(x)')
plt.plot(xx,dfxx,label='$f\'(x)$')

plt.legend()
plt.show()











