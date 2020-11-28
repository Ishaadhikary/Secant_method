import math as m 
import numpy as np 
import tabulate

print ("Enter coefficient of equation:") 
a1= float(input ("Enter the first coefficient a1: "))
a2=float(input ("Enter the second coefficient a2: "))
a3=float(input ("Enter the third coefficient a3: "))
a4=float(input ("Enter the forth coefficient a4: "))

def f(x): 
    return a1*x*x*x + a2*x*x + a3*x+ a4 #error


print("Enter tolerance level : ")
tolerance =float(input ("tolerance:"))
print("Input 1st initial guess:")
a= float(input ("a :"))
print("Input 2nd initial guess:")
b= float(input ("b: "))
nos=1
while (float(m.sqrt(f(a)*f(a))) > tolerance): #error
    x1 = (a*f(b)-b*f(a))/(f(b) - f(a))
    a=b
    b=x1
    nos=nos+1

rounded= round(a,4)
print ("The required root is ",rounded)
