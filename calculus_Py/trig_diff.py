# DERIVATIVE OF TRIGONOMETRIC FUNCTIONS USING SYMPLOT

# LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import sympy.plotting.plot as symplot

x = sym.symbols('x')
i = input('f(x) = ')
f = sym.sympify(i)
df = sym.diff(f)

p = symplot(f,(x,0,10),show=False)
p.extend(symplot(df,(x,0,10),show=False))
p[1].line_color = 'r'
p[0].label = '$f(x) = %s $'%sym.latex(f)
p[1].label = '$f\'(x) = %s$'%sym.latex(df)

p.legend = True
p.show()
















