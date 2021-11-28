# DOUBLE INTEGRATION

# LIBRARIES
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x,y = sym.symbols('x,y')
fxy = x**2 * (sym.sin(y)/sym.cos(y))

i1 = sym.integrate(fxy ,x)
i2 = sym.integrate(i1 ,y)

p = sym.plotting.plot3d(fxy ,(x,-10,10) ,(y,-10,10),title = '$f(x,y)= %s $'%sym.latex(fxy))
p = sym.plotting.plot3d(i2 ,(x,-10,10) ,(y,-10,10),title = '$\int\int %s dxdy =%s+C$'%(sym.latex(fxy),sym.latex(i2)))
