print()

print("This app is supposed to calculate slopes of lines that pass through")
print("two (non-vertical) points.")

print()

x1, y1 = eval(input("Enter the first point's x and y coordinates (respectively), seperated by a comma: "))

x2, y2 = eval(input("Enter the second point's x and y coordinates (respectively), seperated by a comma: "))

M = (y2 - y1) / (x2 - x1)

print()

print("The slope is", M)
