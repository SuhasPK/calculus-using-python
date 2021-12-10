# #   LIMIT OF A FUNCTION
#
# # LIBRARIES
# import matplotlib.pyplot as plt
# import sympy as sym
# import numpy as np
#
#
# x = sym.symbols('x')
# i = input('f(x) = ')
#
# fx = sym.sympify(i)
# lim_pnt = float(input('limit point = '))
#
# limit = sym.limit(fx,x,lim_pnt)
# print('limit $%s$ at %g = %g '%(sym.latex(fx),lim_pnt,limit))
# print(' ')
# print('Please specify x-range and y-range for plotting.')
# xmin = float(input('x minimum = '))
# xmax = float(input('x maximum = '))
# ymin = float(input('y minimum = '))
# ymax = float(input('y maximum = '))
#
# # plotting
# fxx = sym.lambdify(x,fx)
# xx = np.linspace (xmin,xmax,500)
#
# plt.plot(xx ,fxx(xx),label='f(x)= $%s$'%sym.latex(fx))
# plt.plot(lim_pnt ,limit ,'ro',label = '$\lim_{x \\to %g}%s  = %g$'%(lim_pnt,fx,limit))
#
#
# plt.axis ((xmin,xmax,ymin,ymax))
# plt.grid ()
# plt.legend ()
# plt.show ()
#
###############################################################################

#   LIMIT OF A FUNCTION

# LIBRARIES
import matplotlib.pyplot as plt
import sympy as sym
import numpy as np
from matplotlib.figure import Figure
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
#  To combine mathplotlib with tkinter


def limits():

    global function_label, limit_point_label, function_entry, limit_point_entry

    x = sym.symbols('x')
    function = sym.sympify(str(function_entry.get()))
    limit_point = int(limit_point_entry.get())
    limit = sym.limit(function, x, limit_point)
    fxx = sym.lambdify(x, function)
    xmax = limit_point*2
    ymax = sym.limit(function, x, limit_point+1)    # range for the graph
    xx = np.linspace(0, int(xmax), 500)

    # To plot the graph and display it along with tkinter
    graph = Figure(figsize=(5, 5), dpi=100)
    a = graph.add_subplot(111)
    a.plot(xx, fxx(xx), label='f(x)= $%s$' % sym.latex(function))
    a.plot(limit_point, limit, 'ro',
           label='$\lim_{x \\to %g}%s = %g$' % (limit_point, function, limit))

    a.axis((0, int(xmax), 0, int(ymax)))
    a.grid()
    a.legend()
    canvas = FigureCanvasTkAgg(graph, master=root)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack()


root = Tk()
root.title("Limits *Work under progress*")
back = Canvas(root, height=500, width=500)
# Not working as intended. need to check.
function_label = Label(back, text='Enter the funtion f(x): ')
function_label.grid(row=0, column=0, sticky='w', ipadx=10, ipady=8, padx=1, pady=1)
limit_point_label = Label(back, text='Enter the limit point: ')
limit_point_label.grid(row=1, column=0, sticky='w', ipadx=10, ipady=8, padx=1, pady=1)
function_entry = Entry(back)
function_entry.grid(row=0, column=1, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)
limit_point_entry = Entry(back)
limit_point_entry.grid(row=1, column=1, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)
calculate_button = Button(back, text='Calculate', command=lambda: limits()).grid(
    row=2, column=0, columnspan=2, sticky='ew', ipadx=10, ipady=8, padx=1, pady=1)
back.pack()
root.mainloop()
