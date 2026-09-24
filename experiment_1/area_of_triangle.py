#WAP to enter three side of triangle and find out the area of the triangle
import math
x=int(input("enter a 1st side:"))
y=int(input("enter a 2nd side:"))
z=int(input("enter a 3rd side:"))
s=(x+y+z)/2
Ar= math.sqrt(s*(s-x)*(s-y)*(s-z))
print("area of triangle is:",Ar)


