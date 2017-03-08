import math

def pizzaPricePerArea(D, P):
    A = (math.pi * D ** 2) / 4
    return P / A

print("This program calculates the cost per square unit area of a circular")
print("pizza given its diameter.")
print()
D = float(input("What's the pizza diameter: "))
P = float(input("What's the pizza price: "))
PPA = pizzaPricePerArea(D, P)
print()
print("The cost per square unit area is ${:0.3f}".format(PPA))
