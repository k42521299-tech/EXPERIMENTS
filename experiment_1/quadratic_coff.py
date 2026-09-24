#WAP to enter cofficient of a quadratic equation and find ot its roots
#import math as mt
import cmath as mt
x=int(input("enter 1st cofficient:"))
y=int(input("enter 2nd cofficient:"))
z=int(input("enter 3rd cofficient:"))
#d = mt.sqrt((y**2) - (4*x*z))
d = (y**2) - (4*x*z)
root1= (-y + (mt.sqrt(d)))/(2*x)
root2 = (-y - (mt.sqrt(d)))/(2*x)
print("root1:",root1)
print("root2:",root2)

