
# LIBRARIES

import matplotlib.pyplot as plt
import sympy as sym
import numpy as np
from IPython.display import display, Math
from matplotlib.patches import Polygon
from scipy.signal import find_peaks
import sympy.plotting.plot as symplot
from sympy import symbols
from tkinter import *
from tkinter import ttk

###############################################################################

# # LIMIT OF A FUNCTION (1_lmits.py)
#
#
# def lim_fun():
#
#     x = sym.symbols('x')
#     fx = input("Enter the function f(x): ")
#     lim_pnt = 1.5
#     lim = sym.limit(fx, x, lim_pnt)
#     print('\nLimit: ', format(lim, '.4f'), '\n')
#     display(Math('\\lim_{x\\to%g} %s = %g ' % (lim_pnt, sym.latex(fx), lim)))
#
#     # ploting
#
#     fxx = sym.lambdify(x, fx)
#     xx = np.linspace(-5, 5, 500)
#     plt.plot(xx, fxx(xx), label='f(x)')
#     plt.plot(lim_pnt, lim, 'ro')
#     plt.axis('square')
#     plt.axis((-7, 7, -7, 7))
#     plt.grid()
#     plt.legend()
#     plt.show()
#
# ###############################################################################
#
# # (area.py)
#
#
# def area():
#     x = sym.symbols('x')
#     symf = symbols(input("Enter the function f(x): "))
#     symg = symbols(input("Enter the function g(x): "))
#     f = sym.lambdify(x, symf)
#     g = sym.lambdify(x, symg)
#     fg_intersect = sym.solve(symf-symg)
#     A = sym.integrate(symf-symg, (x, fg_intersect[0], fg_intersect[1]))
#     xx = np.linspace(-5, 5, 500)
#     xvalues = np.linspace(0, 1, 100)
#     points = np.vstack((g(xvalues), f(xvalues))).T
#     p = Polygon(points, facecolor='yellow', alpha=0.5)
#     fig, ax = plt.subplots()
#     ax.add_patch(p)
#
#     plt.plot(xx, f(xx))
#     plt.plot(xx, g(xx),  'r')
#     plt.legend(['$f(x)=%s$' % sym.latex(symf), '$g(x)=%s$' % sym.latex(symg)])
#     plt.axis([-3, 5, -3, 5])
#     plt.title('The area between the two curves = %g' % abs(A))
#     plt.grid()
#     plt.show()
#
#
# area()
# ###############################################################################
#
# # AREA BETWEEN TWO CURVES (area2.py)
#
#
# def area1():
#
#     x = sym.symbols('x')
#     f = x**2
#     g = x+2
#     h = f-g
#     xx = np.linspace(-3, 3, 200)
#     y1 = sym.lambdify(x, f)(xx)
#     y2 = sym.lambdify(x, g)(xx)
#
#     # this gives the intersecting points.
#     idx = np.argwhere(np.diff(np.sign(y1-y2)) != 0)
#
#     x1 = xx[idx][0]
#     x2 = y1[idx][1]
#     print(x1, x2)
#
#     A = abs(sym.integrate(h, (x, x1, x2)))
#     # this give the area.
#     with plt.xkcd():
#         fig, ax = plt.subplots()
#         ax.fill_between(xx, y1, y2, where=y2 >= y1, facecolor='green')
#         # shades the area
#         plt.plot(xx, y1, label='$f(x)=%s$' % sym.latex(f))
#         plt.plot(xx, y2, label='$g(x)=%s$' % sym.latex(g))
#         plt.plot(xx[idx], y1[idx], 'ro')
#         plt.legend()
#         plt.title('The area between the two curves is %.4f square units.' % A)
#         plt.show()
#
# ###############################################################################
#
# # FINDING CRITICAL POINTS OF A FUNCTION (critical1.py)
#
#
# def critical():
#
#     x = np.linspace(-4, 4, 1001)
#     fx = x**2 * np.exp(-x**2)
#     dfx = np.diff(fx)/(x[1]-x[0])
#     localmax = find_peaks(fx)[0]
#     localmin = find_peaks(-fx)[0]
#
#     with plt.xkcd():
#         plt.plot(x, fx, label='f(x)')
#         plt.plot(x[0:-1], dfx, label='$f\'(x)$')
#         plt.plot(x[localmax], fx[localmax], 'ko', label='maxima')
#         plt.plot(x[localmin], fx[localmin], 'ro', label='minima')
#         plt.legend()
#         plt.show()
#
# ###############################################################################
#
# # TO FIND CRITICAL POINTS OF A GIVEN FUNCTION - SUMBOLIC METHOD (critical2.py)
#
#
# def critical2():
#
#     x = sym.symbols('x')
#     fx = x**2 * sym.exp(-x**2)
#     dfx = sym.diff(fx)
#     critical_points = sym.solve(dfx)
#
#     xx = np.linspace(-4, 4, 1001)
#     fxx = sym.lambdify(x, fx)(xx)
#     dfxx = sym.lambdify(x, dfx)(xx)
#
#     print('critical points are ' + str(critical_points))
#
#     # EXERCISE : PLOT THE CRITICAL POINTS ON THE GIVEN FUNCTION CURVE.
#     plt.plot(xx, fxx, label='f(x)')
#     plt.plot(xx, dfxx, label='$f\'(x)$')
#     plt.legend()
#     plt.show()
#
# ###############################################################################
#
# # INTEGRATION OF A POLYNOMIAL (integrate.py)
#
#
# def integrate():
#     x = sym.symbols('x')
#     fx = x**2
#     # Indefinite integration
#     idi = sym.integrate(fx)
#
#     xx = np.linspace(-4, 4, 1000)
#     fxx = sym.lambdify(x, fx)(xx)
#     idi_xx = sym.lambdify(x, idi)(xx)
#
#     plt.plot(xx, fxx, label='$f(x)=%s$' % sym.latex(fx))
#     plt.plot(xx, idi_xx, label='$ \int %s dx = %s+C $' %
#              (sym.latex(fx), sym.latex(idi)))
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Indefinite integration')
#     plt.grid()
#     plt.legend()
#     plt.show()
#
# ###############################################################################
#
# # INTEGRATION OF A TRIGONOMETRIC FUNCTION (integrate1.py)
#
#
# def trigno_integrate():
#     x = sym.symbols('x')
#     fx = sym.cos(x)
#
#     idi = sym.integrate(fx)
#
#     xx = np.linspace(0, 2*np.pi, 1000)
#     fxx = sym.lambdify(x, fx)(xx)
#     idi_xx = sym.lambdify(x, idi)(xx)
#
#     plt.plot(xx, fxx, label='$f(x)=%s$' % (sym.latex(fx)))
#     plt.plot(xx, idi_xx, label='$ \int %s dx = %s+C$' %
#              (sym.latex(fx), sym.latex(idi)))
#
#     plt.xlabel('x')
#     plt.ylabel('y')
#
#     plt.grid()
#     plt.legend()
#     plt.show()
#
# ###############################################################################
#
# # DEFINITE INTEGRATION (integrate2.py)
#
#
# def definate_integrate():
#     x = sym.symbols('x')
#     fx = x**3
#     di = sym.integrate(fx, (x, 1, 2))
#     p = symplot(fx, show=False)
#     p[0].label = '$f(x)=%s$ ' % sym.latex(fx)
#     p.title = '$ \int_{1}^{2} %s dx = %g$' % (sym.latex(fx), di)
#     p.xlim = [-3, 3]
#     p.ylim = [-10, 10]
#     p.legend = True
#     p.show()
#
# ###############################################################################
#
# # PARTIAL DERIVATIVE (part_der.py)
#
#
# def partial_derivative():
#
#     x, y = sym.symbols('x y')
#     fxy = x**3 + (x**2)*(y**4)
# # partial deerivative with respect to x.
#     fdx = sym.diff(fxy, x)
# # partial derivative with respect to y.
#     fdy = sym.diff(fxy, y)
# # plotting
#     p = sym.plotting.plot3d(fxy, (x, -3, 3), (y, -3, 3),
#                             title='$f(x,y)=%s$' % (sym.latex(fxy)))
#     p = sym.plotting.plot3d(fdx, (x, -3, 3), (y, -3, 3),
#                             title='$f(x,y)=%s$' % (sym.latex(fdx)))
#     p = sym.plotting.plot3d(fdy, (x, -3, 3), (y, -3, 3),
#                             title='$f(x,y)=%s$' % (sym.latex(fdy)))
#     p.show()
#
# ###############################################################################
#
# #   PIECEWISE FUNCTION (piecewise_function.py)
#
#
# def piecewise_function():
#
#     x = sym.symbols('x')
#     piece1 = 0
#     piece2 = -2*x
#     piece3 = (x**3)/10
#     fx = sym.Piecewise((piece1, x < 0), (piece2, (x >= 0)
#                        & (x < 10)), (piece3, x >= 10))
#
#     fxx = sym.lambdify(x, fx)
#     xx = np.linspace(-3, 20, 1234)
#     plt.plot(xx, fxx(xx))
#     plt.show()
#
# ###############################################################################
#
# #   PIECEWISE FUNCTION 2 (piecewise_function2.py)
#
#
# def piecewise_function2():
#
#     x = sym.symbols('x')
#     f1 = x**3
#     f2 = sym.log(x, 2)
#     fx = sym.Piecewise((f1, x <= 0), (f2, x > 0))
#     fxx = sym.lambdify(x, fx)
#     xx = np.linspace(-3, 15, 1000)
#
#     with plt.xkcd():
#         plt.plot(xx, fxx(xx))
#         plt.xlim([-2, 2])
#         plt.ylim([-10, 3])
#         plt.show()
#
# ###############################################################################
#
# # TO FIND THE DERIVATIVE OF THE POLYNOMAIL (poly_diff.py)
#
#
# def poly_derive():
#
#     x = sym.symbols('x')
#     fx = x**2
#     dfx = sym.diff(fx)
#     fxx = sym.lambdify(x, fx)
#     dfxx = sym.lambdify(x, dfx)
#     xx = np.linspace(-5, 5, 1000)
#     p = symplot(fx, (x, -5, 5), show=False)
#     p.extend(symplot(dfx, (x, -5, 5), show=False))
#     p[1].line_color = 'r'
#     p[0].label = '$f(x) = %s$' % sym.latex(fx)
#     p[1].label = '$f\'(x) = %s$' % sym.latex(dfx)
#     p.legend = True
#     p.ylim = [-10, 10]
#     p.xlim = [-3, 3]
#     p.show()
#
# ###############################################################################
#
# # DERIVATIVE OF A POLYNOMIAL USING MATPLOTLIB (poly_diff1.py)
#
#
# def poly_derive2():
#
#     x = sym.symbols('x')
#     fx = x**2
#     dfx = sym.diff(fx)
#     fxx = sym.lambdify(x, fx)
#     dfxx = sym.lambdify(x, dfx)
#     xx = np.linspace(-5, 5, 1000)
#
#     with plt.xkcd():
#         plt.plot(xx, dfxx(xx), label='$f\'(x) = %s$' % (sym.latex(dfx)))
#         plt.plot(xx, fxx(xx), 'r', label='$f(x) = %s$' % (sym.latex(fx)))
#
#         plt.legend()
#     plt.show()
#
# ###############################################################################
#
# # TANGENT LINES (tangentline.py)
#
#
# def tangent_line():
#
#     x = sym.symbols('x')
#
#     # defining the function.
#     fx = x**3
#
#     # taking the derivative of the function.
#     dfx = sym.diff(fx)
#
#     # the value at which to compute the tangent line.
#     a = 1
#
#     # get the function and derivative value at the point 'a'.
#     fa = fx.subs(x, a)
#     dfa = dfx.subs(x, a)
#
#     xx = np.linspace(-2, 2, 500)
#     f_fun = sym.lambdify(x, fx)(xx)
#     df_fun = sym.lambdify(x, dfx)(xx)
#
#     # the tangent line.
#     tanline = dfa * (xx-a) + fa
#
#     # plotting
#     with plt.xkcd():
#         plt.plot(xx, f_fun, label='$f(x)=%s$' % sym.latex(fx))
#         plt.plot(xx, tanline, label='tangent')
#         plt.plot(a, fa, 'ro', label='a=%g' % a)
#
#         plt.legend(loc='best')
#     plt.title('The Tangent line ')
#     plt.axis('square')
#     plt.axis([-2, 2, -0.5, 2])
#     ax = plt.gca()
#     plt.plot(ax.get_xlim(), [0, 0], 'k--')
#     plt.plot([0, 0], ax.get_ylim(), 'k--')
#     plt.show()
#
# ###############################################################################

root = Tk()
root.title("Calculator")
calculator = ttk.Notebook(root)
calculator.pack()

basic_mode = Frame(calculator)
advance_mode = Frame(calculator)
basic_mode.pack()
advance_mode.pack()

calculator.add(basic_mode, text="Basic mode")
calculator.add(advance_mode, text="Advance mode (*To-do)")

output_display = Entry(basic_mode, justify='center')
input_display = Entry(basic_mode)

input_display.grid(row=0, column=0, columnspan=6, ipadx=10,
                   sticky='ew', ipady=10, padx=5, pady=5)
output_display.grid(row=1, column=0, columnspan=6, ipadx=10,
                    sticky='ew', ipady=10, padx=5, pady=5)


def button_click(number):
    current = input_display.get()
    input_display.delete(0, END)
    input_display.insert(0, str(current) + str(number))
    return


def clear_button():
    input_display.delete(0, END)
    return


def delete_button():
    current = input_display.get()
    current = current[0:-1]
    input_display.delete(0, END)
    input_display.insert(0, current)
    return

# Number buttons


button_0 = Button(basic_mode, text="0", command=lambda: button_click(0))
button_1 = Button(basic_mode, text="1", command=lambda: button_click(1))
button_2 = Button(basic_mode, text="2", command=lambda: button_click(2))
button_3 = Button(basic_mode, text="3", command=lambda: button_click(3))
button_4 = Button(basic_mode, text="4", command=lambda: button_click(4))
button_5 = Button(basic_mode, text="5", command=lambda: button_click(5))
button_6 = Button(basic_mode, text="6", command=lambda: button_click(6))
button_7 = Button(basic_mode, text="7", command=lambda: button_click(7))
button_8 = Button(basic_mode, text="8", command=lambda: button_click(8))
button_9 = Button(basic_mode, text="9", command=lambda: button_click(9))

# Other buttons

button_plus = Button(
    basic_mode, text="+", command=lambda: button_click('+'))

button_minus = Button(
    basic_mode, text="-", command=lambda: button_click('-'))

button_dot = Button(basic_mode, text=".",  command=lambda: button_click('.'))

button_cross = Button(
    basic_mode, text="x", command=lambda: button_click('x'))

button_bar = Button(basic_mode, text="/", command=lambda: button_click('/'))

button_percent = Button(
    basic_mode, text="%", command=lambda: button_click('%'))

button_clear = Button(
    basic_mode, text="AC", command=lambda: clear_button())

button_delete = Button(
    basic_mode, text="DEL", command=lambda: delete_button())

button_bracket_open = Button(
    basic_mode, text="(", command=lambda: button_click('('))

button_bracket_close = Button(basic_mode, text=")",
                              command=lambda: button_click(')'))

button_square = Button(
    basic_mode, text="^", command=lambda: button_click('^('))

button_sqrt = Button(
    basic_mode, text="sqrt", command=lambda: button_click('sqrt('))

button_equals = Button(
    basic_mode, text="=", command=lambda: button_click('='))

# Button arrangements
# Row 1

button_7.grid(row=2, column=0, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)
button_8.grid(row=2, column=1, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)
button_9.grid(row=2, column=2, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)

button_bar.grid(row=2, column=3, sticky='ew',
                ipadx=10, ipady=8, padx=1, pady=1)

button_delete.grid(row=2, column=4, sticky='ew',
                   ipadx=10, ipady=8, padx=1, pady=1)

button_clear.grid(row=2, column=5, sticky='ew', ipadx=10, ipady=8)

# Row 2

button_4.grid(row=3, column=0, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)
button_5.grid(row=3, column=1, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)
button_6.grid(row=3, column=2, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)
button_cross.grid(row=3, column=3, sticky='ew',
                  ipadx=10, ipady=8, padx=1, pady=1)

button_bracket_open.grid(row=3, column=4, sticky='ew',
                         ipadx=10, ipady=8, padx=1, pady=1)

button_bracket_close.grid(row=3, column=5, sticky='ew',
                          ipadx=10, ipady=8, padx=1, pady=1)

# Row 3

button_1.grid(row=4, column=0, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)
button_2.grid(row=4, column=1, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)
button_3.grid(row=4, column=2, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)

button_minus.grid(row=4, column=3, sticky='ew',
                  ipadx=10, ipady=8, padx=1, pady=1)

button_square.grid(row=4, column=4, sticky='ew',
                   ipadx=10, ipady=8, padx=1, pady=1)

button_sqrt.grid(row=4, column=5, sticky='ew',
                 ipadx=10, ipady=8, padx=1, pady=1)

# Row 4

button_0.grid(row=5, column=0, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)

button_dot.grid(row=5, column=1, sticky='ew',
                ipadx=10, ipady=8, padx=1, pady=1)

button_percent.grid(row=5, column=2, sticky='ew',
                    ipadx=10, ipady=8, padx=1, pady=1)

button_plus.grid(row=5, column=3, sticky='ew',
                 ipadx=10, ipady=8, padx=1, pady=1)

button_equals.grid(row=5, column=4, columnspan=2,
                   sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)


root.mainloop()
