""" Heating and cooling degree-days are measures used by utility companies to estimate energy requirements. If the average temperature for a day is below 60, then the number of degrees below 60 is added to the heating degree-days. If the temperature is above 80, the amount over 80 is added to the cooling degree-days. Write a program that accepts a sequence of average daily temps and computes the running total of cooling and heating degree-days. The program should print these two totals after all the data has been processed. """

def calc(T):
    d = 0
    l = [0, 0]
    while T != '':
        T = float(T)
        if T < 60:
            l[0] += 60 - T
        elif T > 80:
            l[1] += T - 80
        T = input("\nWhat's the temperature? ")
        d += 1
    print("\nIn {} days, there were {:.0f} heating degree days and {:.0f} cooling degree days.\n".format(d, l[0], l[1]))

def main():
    print("\nThis app computes the number of cooling and heating days.")
    T = input("\nWhat's the temperature? ")
    calc(T)
main()
