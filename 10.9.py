# sphere.py
#    Class definition for a sphere

from math import pi


class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * pi * self.radius ** 3


def main():
    R = float(input("Please enter the radius of the sphere: "))
    print()
    s = Sphere(R)
    V = s.volume()
    A = s.surfaceArea()
    print("The sphere's volume is {}".format(V))
    print("The sphere's surface area is {}".format(A))


if __name__ == "__main__":
    main()
