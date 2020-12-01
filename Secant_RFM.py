import math


"""
print ("Enter coefficient of equation: ax3 + bx2 +cx +d ") 
a1= float(input ("Enter the first coefficient a: "))
a2=float(input ("Enter the second coefficient b: "))
a3=float(input ("Enter the third coefficient c: "))
a4=float(input ("Enter the fourth coefficient d: "))
"""
def f(x):
   
    #return a1*x*x*x + a2*x*x + a3*x+ a4
    return x + math.log(x,10) - 1.2
    #return x**2  +1 
    #return math.sin(x) * math.log(x,10) - math.cos(x)
    #return math.sin(x) * math.exp(10) - math.cos(x)

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

        if iteration > Max:
            print('Not Convergent!')
            quit()

        cond = abs(f(x2)) > tol



    print('\n Hence,The required root is: %0.5f' % x2)
    print('--------------------------------------------')

#initialization
x0 = float(input('Enter first value: '))
x1 = float(input('Enter second value: '))
tol = float(input('Enter the error tolerance: '))

print("The Tolerance Error is:", tol)
Max = int(input('Maximum number of iteration: '))


secant_method(x0, x1, tol, Max)
