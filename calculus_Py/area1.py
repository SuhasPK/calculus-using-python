# AREA BETWEEN TWO CURVES

# LIBRARIES
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


x = sym.symbols('x')
f = x**2
g = x+2

h = f-g


xx = np.linspace(-3,3,200)
y1 = sym.lambdify(x,f)(xx)
y2 = sym.lambdify(x,g)(xx)

# this gives the intersecting points.
idx = np.argwhere(np.diff(np.sign(y1-y2)) != 0)

x1 = xx[idx][0]
x2 = y1[idx][1]
print(x1,x2)

A = abs(sym.integrate(h,(x,x1,x2))) # this give the area.

with plt.xkcd():
    fig,ax = plt.subplots()
    ax.fill_between(xx,y1,y2,where=y2>=y1,facecolor = 'green') # shades the area.

    plt.plot(xx,y1,label='$f(x)=%s$'%sym.latex(f))
    plt.plot(xx,y2,label='$g(x)=%s$'%sym.latex(g))
    plt.plot(xx[idx],y1[idx],'ro')
    plt.legend()
    plt.title('The area between the two curves is %.4f square units.'%A)


plt.show()












