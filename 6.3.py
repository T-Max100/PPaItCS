import math

def sphereArea(radius):
    return 4 * math.pi * radius ** 2

def sphereVolume(radius):
    return (4 / 3) * math.pi * radius ** 3

def main():
    R = float(input("Please enter the radius of the sphere: "))
    print("The sphere's surface area is {}".format(sphereArea(R)))
    print("The sphere's volume is {}".format(sphereVolume(R)))
main()
