# IPO pattern, i.e. Input, Process, Output. In this case the input will be the radius that the user supplies, the process will be the application of the math formulae to the radius, and the output will be the volume and surface area of a sphere.

import math

R = float(input("Please enter the radius of the sphere: "))
print()
V = (4 / 3) * (math.pi) * R ** 3
A = 4 * math.pi * R ** 2
print("The sphere's volume is", V)
print("The sphere's surface area is", A)
print()
