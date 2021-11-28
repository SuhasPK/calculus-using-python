# INTEGRATION OF A POLYNOMIAL 

# LIBRARIES
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

x = sym.symbols('x')
fx = x**2

# INDEFINITE INTEGRATION
idi = sym.integrate(fx)

xx = np.linspace(-4,4,1000)
fxx = sym.lambdify(x,fx)(xx)
idi_xx = sym.lambdify(x,idi)(xx)

plt.plot(xx,fxx,label='$f(x)=%s$'%sym.latex(fx))
plt.plot(xx,idi_xx,label='$ \int %s dx = %s+C $ '%(sym.latex(fx),sym.latex(idi)))

plt.xlabel('x')
plt.ylabel('y')
plt.title('Indefinite integration')
plt.grid()
plt.legend()
plt.show()












