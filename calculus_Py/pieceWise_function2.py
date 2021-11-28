#   PIECEWISE FUNCTION

#   LIBEARIES
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

x = sym.symbols('x')
f1 = x**3
f2 = sym.log(x,2)



fx = sym.Piecewise( (f1, x<=0) , (f2, x>0 ) )

fxx = sym.lambdify(x,fx)
xx = np.linspace(-3,15,1000)

with plt.xkcd():
    plt.plot(xx,fxx(xx))

plt.xlim([-2,2])
plt.ylim([-10,3])
plt.show()









