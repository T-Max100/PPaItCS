import math

print()

print("This app determines the length of a ladder required to reach a")
print("given height when leaned against a house.")

print()

H = float(input("Please enter the height the ladder needs to reach: "))
G = (math.pi * float(input("Please enter the angle of the ladder as measured from the ground: "))) / 180

L = H / math.sin(G)

print()

print("The length of the required ladder is", round(L,3))

print()
