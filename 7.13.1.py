def DayofYear(date):
    month = int(date[:2])
    day = int(date[3:5])
    year = int(date[6:10])
    dayNum = 0
    if dateValidator(date) == True:
        if LeapYear(year) == True and month >= 3:
            dayNum = (31 * (month - 1) + day) - ((4 * month + 23)//10) + 1
        elif month >= 3:
            dayNum = (31 * (month - 1) + day) - ((4 * month + 23)//10)
        else:
            dayNum = (31 * (month - 1) + day)
    return dayNum

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
    status = False
    if 1 <= year:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= day <= 31:
                status = True
            else:
                status = False
        elif month in [4, 6, 9, 11]:
            if 1 <= day <= 30:
                status = True
            else:
                status = False
        elif month == 2:
            if LeapYear(year) == True and 1 <= day <= 29:
                status = True
            elif LeapYear(year) == False and 1 <= day <= 28:
                status = True
            else:
                status = False
    return status

def main():
    print()
    print("This app tells you the number of the day in a year.\n")
    D = input("What's the date? Enter as mm/dd/yyyy\n\n")
    try:
        print("The day of the year is {}".format(DayofYear(D)))
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
