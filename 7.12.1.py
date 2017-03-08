def LeapYear(year):
    status = False
    if year % 100 == 0 and year % 400 == 0:
        status = True
    elif year % 100 == 0 and year % 400 != 0:
        status = False
    elif year % 4 == 0:
        status = True
    else:
        status = False
    return status

def dateValidator(date):
    month = int(date[:2])
    day = int(date[3:5])
    year = int(date[6:10])
    if 1 <= year:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= day <= 31:
                print("\n{}/{}/{} is a valid date".format(month, day, year))
            else:
                print("\n{}/{}/{} is not a valid date".format(month, day, year))
        elif month in [4, 6, 9, 11]:
            if 1 <= day <= 30:
                print("\n{}/{}/{} is a valid date".format(month, day, year))
            else:
                print("\n{}/{}/{} is not a valid date".format(month, day, year))
        elif month == 2:
            if LeapYear(year) == True and 1 <= day <= 29:
                print("\n{}/{}/{} is a valid date".format(month, day, year))
            elif LeapYear(year) == False and 1 <= day <= 28:
                print("\n{}/{}/{} is a valid date".format(month, day, year))
            else:
                print("\n{}/{}/{} is not a valid date".format(month, day, year))

def main():
    print()
    print("This app validates dates you enter.\n")
    D = input("What's the date? Enter as mm/dd/yyyy\n\n")
    try:
        dateValidator(D)
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
