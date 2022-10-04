#This program will solve a quadratic equation

import math

a = 10
b = 100
c = 3

d = (b**2) - (4*a*c)

p = (-b + math.sqrt(d)) / (2*a)
pn = (-b - math.sqrt(d)) / (2*a)

print("The solution for the quadratic equation is:")
print(p)
print(pn)