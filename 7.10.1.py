def easter(year):
    if 1900 <= year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b +4 * c + 6 * d + 5) % 7
        if year in [1954, 1981, 2049, 2076]:
            if d + e <= 9:
                print("Easter falls on March {}, in the year {}.".format((15 + d + e), year))
            else:
                print("Easter falls on April {}, in the year {}.".format(((d + e) - 16), year))
        elif d + e <= 9:
            print("Easter falls on March {}, in the year {}.".format((22 + d + e), year))
        else:
            print("Easter falls on April {}, in the year {}.".format(((d + e) - 9), year))
    else:
        print("The year {} is out of range.".format(year))

def main():
    print()
    print("This app predicts the date of Easter given a year between 1900 and 2099.\n")
    Y = int(input("What year do you want to know the date of Easter for?: "))
    print()
    easter(Y)
    print()
main()
