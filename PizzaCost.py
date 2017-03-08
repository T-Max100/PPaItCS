import math

print("This program calculates the cost per square unit area of a circular")
print("pizza given its diameter.")
print()
D = float(input("What's the pizza diameter: "))
P = float(input("What's the pizza price: "))
A = (math.pi * D ** 2) / 4
PPA = P / A
print()
print("the cost per square unit area is", round(PPA,2))
