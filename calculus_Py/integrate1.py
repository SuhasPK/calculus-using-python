# INTEGRATION OF A TRIGONOMETRIC FUNCTION

# LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym


x = sym.symbols('x')
fx = sym.cos(x)

idi = sym.integrate(fx)

xx = np.linspace(0,2*np.pi,1000)
fxx = sym.lambdify(x,fx)(xx)
idi_xx = sym.lambdify(x,idi)(xx)

plt.plot(xx,fxx, label='$f(x)=%s$'%(sym.latex(fx)))
plt.plot(xx,idi_xx, label='$ \int %s dx = %s+C$'%(sym.latex(fx),sym.latex(idi)))

plt.xlabel('x')
plt.ylabel('y')

plt.grid()
plt.legend()
plt.show()

















