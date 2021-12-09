# EXERCISE-1

# LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import sympy.plotting.plot as symplot

x,a = sym.symbols('x,a')
print("Let the independent variable be 'x' and a costant be 'a' which varies from 0 to 3. ")
i = input('f(x) = ')
color = 'brkm'
fx = sym.sympify(i)



for ai in range(0,4):
    if ai==0:
        p = symplot(fx.subs(a,ai),show=False,label='a='+str(ai),line_color=color[0])
    else:
        p.extend(symplot(fx.subs(a,ai),show=False,label='a='+str(ai),line_color=color[ai]))
p.title = 'The functions'
p.legend = True
p.show()

for ai in range(0,4):
    if ai==0:
        g = symplot(sym.diff(fx.subs(a,ai)),show=False,label='a='+str(ai),line_color=color[0])
    else:
        g.extend(symplot(sym.diff(fx.subs(a,ai)) , show=False , label='a='+str(ai) , line_color=color[ai]))

g.title = 'Their derivatives'
g.legend = True
g.show()


