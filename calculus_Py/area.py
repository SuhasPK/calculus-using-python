import sympy as sym
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

x = sym.symbols('x')

symf = x**2
symg = x

f = sym.lambdify(x,symf)
g = sym.lambdify(x,symg)

fg_intersect = sym.solve(symf-symg)
A = sym.integrate(symf-symg,(x,fg_intersect[0],fg_intersect[1]))

xx = np.linspace(-5,5,500)



xvalues = np.linspace(0,1,100)
points = np.vstack((g(xvalues),f(xvalues))).T
p = Polygon(points,facecolor='yellow',alpha=.5)

fig, ax = plt.subplots()
ax.add_patch(p)

plt.plot(xx,f(xx))
plt.plot(xx,g(xx),'r')



plt.legend(['$f(x)=%s$'%sym.latex(symf),'$g(x)=%s$'%sym.latex(symg)])
plt.axis([-3,5,-3,5])
plt.title('The area between the two curves = %g'%abs(A))
plt.grid()
plt.show()


