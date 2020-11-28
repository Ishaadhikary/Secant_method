import math
import numpy
import tabulate


def f(x):
    #return x**3 + 5*x**2 - 2*x + 10
    return x * math.log(x,10) - 1.2


def secant_method(x0, x1, tol, Max):
    print('\n\n*** SECANT ROOT FINDING METHOD***')
    print('--------------------------------------------')
    iteration = 1
    cond = True
    while cond:
        if f(x0) == f(x1):
            print('Error!')
            quit()
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Iteration: %d, x2 = %0.5f and f(x2) = %0.5f' % (iteration, x2, f(x2)))
        x0 = x1
        x1 = x2
        iteration = iteration + 1
        cond = abs(f(x2)) > tol

    print('\n Hence,The required root is: %0.5f' % x2)
    print('--------------------------------------------')

#initialization
x0 = float(input('Enter first value: '))
x1 = float(input('Enter second value: '))
tol = float(input('Enter the error tolerance: '))

print("The Tolerance Error is:", tol)
Max = int(input('Total number of iteration: '))


secant_method(x0, x1, tol, Max)
