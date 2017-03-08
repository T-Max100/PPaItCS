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
    print(month)
    day = int(date[3:5])
    print(day)
    year = int(date[6:10])
    print(year)
    if 1 <= year:
        if month == 1:
            if 1 <= day <= 31:
                print("{}/{}/{} is a valid date".format(month, day, year))
            else:
                print("{}/{}/{} is not a valid date".format(month, day, year))
        if month == 2:
            if LeapYear(year) == True and 1 <= day <= 29:
                print("{}/{}/{} is a valid date".format(month, day, year))
            elif LeapYear(year) == False and 1 <= day <= 28:
                print("{}/{}/{} is a valid date".format(month, day, year))
            else:
                print("{}/{}/{} is not a valid date".format(month, day, year))
        if month == 3:
            if 1 <= day <= 31:
                print("{}/{}/{} is a valid date".format(month, day, year))
            else:
                print("{}/{}/{} is not a valid date".format(month, day, year))
