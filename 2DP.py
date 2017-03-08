print()

print("This program calculates the distance between two points on a plane.")

print()

x1, y1 = eval(input("Enter the first point's x and y coordinates (respectively), seperated by a comma: "))

x2, y2 = eval(input("Enter the second point's x and y coordinates (respectively), seperated by a comma: "))

D = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print()

print("The distance is", D)

print()
