def main():
    print("This program is designed to convert distances.")

    Km = eval(input("What's the distance in kilometers?: "))

    miles = Km / 1.609344

    print("That distance in miles is", miles, "miles.")

main()
