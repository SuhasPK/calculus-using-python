# FUNDAMENTAL THEOREM OF CALCULUS

# LIBRARIES
import sympy as sym


x = sym.symbols('x')
fx = 2*x + sym.cos(x)

# integrate(differentiate(function))
dfx1 = sym.diff(fx)
idf1 = sym.integrate(dfx1)

# differentiate(integrate(function))
idf2 = sym.integrate(fx)
dfx2 = sym.diff(idf2)

if idf1==fx and dfx2==fx :
    print('The fundamental theorem of calculus holds true.')
else:
    print('The fundamental theorem of calculus holds false.')
















