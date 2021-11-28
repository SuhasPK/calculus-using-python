# TRAPEZOIDAL METHOD

# LIBRARIES

# to define a function.
def f(x):
    return 1/(1 + x**2)

def trapezoidal(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
    
    # Finding final integration value
    integration = integration * h/2
    



    return integration
    

lower_limit = float(input("lower limit = "))
upper_limit = float(input("upper limit = "))
sub_interval = int(input("sub interval = "))


result = trapezoidal(lower_limit,upper_limit,sub_interval)

print("Integration result by Trapeziodal method is = %0.6f"%(result))


