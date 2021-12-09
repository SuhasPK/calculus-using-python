#   LIMIT OF A FUNCTION

# LIBRARIES
import matplotlib.pyplot as plt
import sympy as sym
import numpy as np


x = sym.symbols('x')
i = input('f(x) = ')

fx = sym.sympify(i)
lim_pnt = float(input('limit point = '))

limit = sym.limit(fx,x,lim_pnt)
print('limit $%s$ at %g = %g '%(sym.latex(fx),lim_pnt,limit))
print(' ')
print('Please specify x-range and y-range for plotting.')
xmin = float(input('x minimum = '))
xmax = float(input('x maximum = '))
ymin = float(input('y minimum = '))
ymax = float(input('y maximum = '))

# plotting
fxx = sym.lambdify(x,fx)
xx = np.linspace (xmin,xmax,500)

plt.plot(xx ,fxx(xx),label='f(x)= $%s$'%sym.latex(fx))
plt.plot(lim_pnt ,limit ,'ro',label = '$\lim_{x \\to %g}%s  = %g$'%(lim_pnt,fx,limit))


plt.axis ((xmin,xmax,ymin,ymax))
plt.grid ()
plt.legend ()
plt.show ()

















