# FINDING CRITICAL POINTS OF A FUNCTION

# LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks



x = np.linspace(-4,4,1001)
fx = x**2 * np.exp(-x**2)
dfx = np.diff(fx)/(x[1]-x[0])

localmax = find_peaks(fx)[0]
localmin = find_peaks(-fx)[0]

with plt.xkcd():
    plt.plot(x,fx,label='f(x)')
    plt.plot(x[0:-1],dfx,label='$f\'(x)$')
    plt.plot(x[localmax],fx[localmax],'ko',label='maxima')
    plt.plot(x[localmin],fx[localmin],'ro',label='minima')
    plt.legend()

plt.show()
