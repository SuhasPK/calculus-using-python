# DOUBLE INTEGRATION

# LIBRARIES
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x,y = sym.symbols('x,y')
fxy = x + y

i1 = sym.integrate(fxy,x)
i2 = sym.integrate(i1,y)

p = sym.plotting.plot3d(fxy,(x,-3,3),(y,-3,3),title = '$f(x,y)=%s$'%sym.latex(fxy))

p = sym.plotting.plot3d(i2,(x,-3,3),(y,-3,3),title = '$\int\int [%s] dxdy=%s+C$'%(sym.latex(fxy),sym.latex(i2)))













