# PARTIAL DERIVATIVE

# LIBRARIES
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

x,y = sym.symbols('x y')

fxy = x**3 + (x**2)*(y**4)

# partial deerivative with respect to x.
fdx = sym.diff(fxy,x)

# partial derivative with respect to y.
fdy = sym.diff(fxy,y)

# plotting

p = sym.plotting.plot3d(fxy,(x,-3,3),(y,-3,3),title = '$f(x,y)=%s$'%(sym.latex(fxy)) )

p = sym.plotting.plot3d(fdx,(x,-3,3),(y,-3,3),title = '$f(x,y)=%s$'%(sym.latex(fdx)) )

p = sym.plotting.plot3d(fdy,(x,-3,3),(y,-3,3),title = '$f(x,y)=%s$'%(sym.latex(fdy)) )



