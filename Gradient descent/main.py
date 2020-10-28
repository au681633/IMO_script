from sympy import *
import numpy as np

def gradient():
    # first x
    xres = 1

    x = Symbol('x')

    # function
    y = (x-1)**4 + sin(x)**2

    yprime = y.diff(x)
    fprime = lambdify(x, yprime, 'numpy')
    f = lambdify(x, y, 'numpy')
 # ok
    print(y)
    print(yprime)

    print("")

    k = 1

    # only works if the right lambda is chosen

    while abs(fprime(xres)) >= 0.5:
        xres = xres - (2**(-k) * fprime(xres))
        k += 1

    yres = f(xres)

    return("Minimum is at (" + str(xres) + "," + str(yres) + ")")

print(gradient())

