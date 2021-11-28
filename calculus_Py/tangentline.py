# TANGENT LINES

# LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym


x = sym.symbols('x')

# defining the function.
fx = x**3

# taking the derivative of the function.
dfx = sym.diff(fx)

# the value at which to compute the tangent line.
a = 1

# get the function and derivative value at the point 'a'.
fa = fx.subs(x,a)
dfa = dfx.subs(x,a)


xx = np.linspace(-2,2,500)
f_fun = sym.lambdify(x,fx)(xx)
df_fun = sym.lambdify(x,dfx)(xx)

# the tangent line.
tanline = dfa * (xx-a) + fa

# plotting
with plt.xkcd():
    plt.plot(xx,f_fun,label='$f(x)=%s$'%sym.latex(fx))
    plt.plot(xx,tanline,label='tangent')
    plt.plot(a,fa,'ro',label='a=%g'%a)


    plt.legend(loc='best')

plt.title('The Tangent line ')


plt.axis('square')
plt.axis([-2,2,-0.5,2])

ax = plt.gca()
plt.plot(ax.get_xlim(),[0,0],'k--')
plt.plot([0,0],ax.get_ylim(),'k--')

plt.show()










