def LeapYear(year):
    if year % 100 == 0 and year % 400 == 0:
        print("The year {} is a leap year".format(year))
    elif year % 100 == 0 and year % 400 != 0:
        print("The year {} is not a leap year".format(year))
    elif year % 4 == 0:
        print("The year {} is a leap year".format(year))
    else:
        print("The year {} is not a leap year".format(year))

def main():
    print()
    print("This app will tell you if the year you ask about is a leap year.\n")
    Y = int(input("Enter year: "))
    LeapYear(Y)
    print()
main()
