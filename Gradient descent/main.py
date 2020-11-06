from sympy import *
import numpy as np

def gradient():
    # first x
    xres = 1
    x = Symbol('x')
    # function
    y = (x-1)**4 + sin(x)**2
    yprime = y.diff(x)
    # creates function in python
    fprime = lambdify(x, yprime, 'numpy')
    f = lambdify(x, y, 'numpy')
    print(y)
    print(yprime)
    print("")

    # only works if the right lambda is chosen
    while abs(fprime(xres)) >= 0.0001:
        xres = xres - (1/4 * fprime(xres))

    return("Minimum is at (" + str(xres) + "," + str(f(xres)) + ")")

print(gradient())

