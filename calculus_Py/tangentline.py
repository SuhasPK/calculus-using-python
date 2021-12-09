# TANGENT LINES

# LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym


x = sym.symbols('x')
i = input("f(x) =  ")
# defining the function.
fx = sym.sympify(i)

# taking the derivative of the function.
dfx = sym.diff(fx)

# the value at which to compute the tangent line.
a = float(input("The point at which to compute the tangent line =  "))

# get the function and derivative value at the point 'a'.
fa = fx.subs(x,a)
dfa = dfx.subs(x,a)

print(" Please specify the x-range and y-range values.")
xmin = float(input("x minimum = "))
xmax = float(input("x minimum = "))
ymin = float(input("y minimum = "))
ymax = float(input("y maximum = "))


xx = np.linspace(xmin,xmax,500)
f_fun = sym.lambdify(x,fx)(xx)
df_fun = sym.lambdify(x,dfx)(xx)

# the tangent line.
tanline = dfa * (xx-a) + fa

# plotting

plt.plot(xx,f_fun,label='$f(x)=%s$'%sym.latex(fx))
plt.plot(xx,tanline,label='tangent')
plt.plot(a,fa,'ro',label='a=%g'%a)


plt.legend(loc='best')

plt.title('The Tangent line ')

plt.grid()
plt.axis('square')
plt.axis([xmin,xmax,ymin,ymax])

#ax = plt.gca()
#plt.plot(ax.get_xlim(),[0,0],'k--')
#plt.plot([0,0],ax.get_ylim(),'k--')

plt.show()










