from sympy import *
import numpy as np

def newtonRaphson():
    # first x
    xres = 1
    # amount of calc
    amount = 50

    x = Symbol('x')

    # function
    y = (x-1)**4 + sin(x)**2

    yprime = y.diff(x)
    fprime = lambdify(x, yprime, 'numpy')
    f = lambdify(x, y, 'numpy')

    print(y)
    print(yprime)

    print("")
    print("Calculating " + str(amount) + " times")

    for i in range(amount):
        xres = xres - (f(xres)*fprime(xres)**-1)

    yres = f(xres)

    return("Minimum is at (" + str(xres) + "," + str(yres) + ")")

print(newtonRaphson())

