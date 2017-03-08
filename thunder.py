print("This program is designed to determine the distance from a lightning")
print("strike, based on the seconds elapsed from the sight of the flash")
print("to the sound of the thunder.")
print()
T = float(input("How many seconds between the flash and the thunder?: "))
D = T * 1100
D_miles = D // 5280
D_feet = D % 5280
print()
print("The distance is", D, "feet.")
print("Which is", D_miles, "miles and", D_feet, "feet.")
print()
