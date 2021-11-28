#   LIMIT OF A FUNCTION

# LIBRARIES
import matplotlib.pyplot as plt
import sympy as sym
import numpy as np
from IPython.display import display,Math

x = sym.symbols('x')

fx = x**3

lim_pnt = 1.5

lim = sym.limit(fx,x,lim_pnt)
print(lim)

display(Math('\\lim_{x\\to%g} %s = %g '%(lim_pnt,sym.latex(fx),lim)))


# plotting
fxx = sym.lambdify(x,fx)
xx = np.linspace(-5,5,500)

plt.plot(xx,fxx(xx),label='f(x)= $x^{3}$')
plt.plot(lim_pnt,lim,'ro')
plt.axis('square')
plt.axis((-7,7,-7,7))
plt.grid()
plt.legend()
plt.show()
















