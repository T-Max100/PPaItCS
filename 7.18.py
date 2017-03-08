import math

def sphereArea(radius):
    return 4 * math.pi * radius ** 2

def sphereVolume(radius):
    return (4 / 3) * math.pi * radius ** 3

def main():
    try:
        R = float(input("Please enter the radius of the sphere: "))
        if R != abs(R):
            print("Please enter a positive number for the radius.")
        elif R == 0:
            print("Please enter a positive number for the radius.")
        else:
            print("The sphere's surface area is {:.3f}".format(sphereArea(R)))
            print("The sphere's volume is {:.3f}".format(sphereVolume(R)))
    except ValueError:
        print("\nThe numbers you entered weren't quite right…")
    except NameError:
        print("\nOnly numbers please.")
    except TypeError:
        print("\nThe numbers you entered weren't quite right…")
    except SyntaxError:
        print("\nType it correctly next time buddy.")
    except:
        print("\nGeneral error. Terribly sorry.")
    print()
main()
