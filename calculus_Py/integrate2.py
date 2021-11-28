# DEFINITE INTEGRATION

# LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import sympy.plotting.plot as symplot

x = sym.symbols('x')
fx = x**3

di = sym.integrate(fx,(x,1,2))

p = symplot(fx,show=False)


p[0].label = '$f(x)=%s$ '%sym.latex(fx)

p.title = '$\int_{1}^{2} %s dx = %g$'%(sym.latex(fx),di) 
p.xlim = [-3,3]
p.ylim = [-10,10]
p.legend = True
p.show()













