def main():
    print("This program was designed to convert US customary volumes (in cubic feet) to metric volumes in cubic meters and liters.")

    feet = eval(input("What's the volume in cubic feet?: "))

    mto3 = ((0.3048) ** 3) * feet

    L = mto3 * 1000

    print("That volume in cubic meters is", mto3, "and that's", L, "liters.")
main()
