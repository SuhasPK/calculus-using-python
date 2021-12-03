# USER INPUT TEST-2 ##  TRIGONOMETRIC FUNCTIONS ##

# LIBRARIES
import sympy as sym
import sympy.plotting.plot as symplot
import numpy as np

x = sym.symbols('x')
i = input('f(x) = ')

xmin = eval((input('xmin = ')))
xmax = eval((input('xmax = ')))

fx = sym.sympify(i)
dfx = sym.diff(fx)

p = symplot(fx ,(x,xmin,xmax),show=False)
p.extend(symplot(dfx ,(x,xmin,xmax),show=False))
p[1]. line_color = 'r'
p[0]. label='$f(x) = %s$'%sym.latex(fx)
p[1]. label='$f\'(x) = %s$'%sym.latex(dfx)
p.legend = True

p.show ()
