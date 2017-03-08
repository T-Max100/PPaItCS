print()

print("This app calculates the epact.")
print("The epact is the number of days between Jan. 1st and the previous")
print("new moon.")

print()

Y = int(input("Enter the 4-digit year of your choosing: "))

C = Y // 100

epact = ((8 + (C // 4)) - C + ((8 * C + 13) // 25) + 11*(Y % 19)) % 30

print()

print("The epact is", epact, "days.")
