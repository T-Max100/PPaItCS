# cube.py
#    Class definition for a cube


class Cube:

    def __init__(self, side_length):
        self.side_length = side_length

    def getSideLength(self):
        return self.side_length

    def surfaceArea(self):
        return 6 * self.side_length ** 2

    def volume(self):
        return self.side_length ** 3

def main():
    s = float(input("Please enter the side length of the cube: "))
    print()
    c = Cube(s)
    V = c.volume()
    A = c.surfaceArea()
    print("The cube's volume is {}".format(V))
    print("The cube's surface area is {}".format(A))


if __name__ == "__main__":
    main()
