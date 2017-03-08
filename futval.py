# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    years = 0
    print("This program calculates the future value")
    print("of an investment over a specified number of years.")

    principal = eval(input("Enter the initial principal: "))
    #apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years: "))
    FC = eval(input("Enter the fixed contribution that will be made (beginning of period, not end): "))
    rate = eval(input("Enter the annual interest rate: "))
    periods = eval(input("Enter the number of annual compounding periods: "))

    for i in range(years):
        #principal = principal * (1 + apr) + FC
        #A = principal * (1 + (rate / periods)) ** (periods * years)
        P = principal
        r = rate
        n = periods
        t = years
        A = (FC * (((1 + (r / n)) ** (n * t) - 1) / (r / n)) * (1 + (r / n))) + (P * (1 + r / n) ** (n * t))

    #print("The value in ", years, "years is:", principal)
    print("The value in ", years, "years is:", A)

main()
