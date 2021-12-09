# DERIVATIVE OF TRIGONOMETRIC FUNCTIONS USING SYMPLOT

# LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import sympy.plotting.plot as symplot

x = sym.symbols('x')
i = input('f(x) = ')
fx = sym.sympify(i)
dfx = sym.diff(fx)

xx = np.linspace(0,10,1000)
fxx = sym.lambdify(x,fx)
dfxx = sym.lambdify(x,dfx)

with plt.xkcd():
    plt.plot(xx,fxx(xx),'b',label = '$f(x)=%s$'%(sym.latex(fx)))
    plt.plot(xx,dfxx(xx),'r',label = '$f\'(x)=%s$'%(sym.latex(dfx)))

    plt.legend()

plt.axis((0,10,-1.1,1.1))
plt.show()
