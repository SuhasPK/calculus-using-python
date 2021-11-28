# DERIVATIVE OF A POLYNOMIAL USING MATPLOTLIB

# LIBRARIES
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt


x = sym.symbols('x')
fx = x**2

dfx = sym.diff(fx)

fxx = sym.lambdify(x,fx)
dfxx = sym.lambdify(x,dfx)
xx = np.linspace(-5,5,1000)


with plt.xkcd():
    plt.plot(xx,dfxx(xx), label = '$f\'(x) = %s$'%(sym.latex(dfx)))
    plt.plot(xx,fxx(xx),'r',label = '$f(x) = %s$'%(sym.latex(fx)))

    plt.legend()
plt.show()











