#   PIECEWISE FUNCTION

#   LIBRARIES
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x = sym.symbols('x')

piece1 = 0
piece2 = -2*x
piece3 = (x**3)/10

fx = sym.Piecewise((piece1,x<0),(piece2, (x>=0)&(x<10)),(piece3,x>=10 ) )

fxx = sym.lambdify(x,fx)
xx = np.linspace(-3,20,1234)

plt.plot(xx,fxx(xx))

plt.show()























