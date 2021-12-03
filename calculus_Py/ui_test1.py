# USER INPUT TEST-1

# LIBRARIES
import sympy as sym
import sympy.plotting.plot as symplot
import numpy as np


x = sym.symbols('x')
i = input('list function ')
fx = sym.sympify(i)
dfx = sym.diff(fx)
fxx = sym.lambdify(x,fx)
dfxx = sym.lambdify(x,dfx)
xx = np.linspace ( -5 ,5 ,1000)

p = symplot(fx ,(x,-5,5),show=False)
p.extend(symplot(dfx ,(x,-5,5),show=False))
p[1]. line_color = 'r'
p[0]. label='$f(x) = %s$'%sym.latex(fx)
p[1]. label='$f\'(x) = %s$'%sym.latex(dfx)
p.legend = True
p.ylim = [ -10,10]
p.xlim = [-3,3]
p.show ()
