# futval2
#    A program to compute the value of an investment
#    carried years into the future

def main():
    print("This program calculates the future value")
    print("of an investment over a specified number of years.")

    P = float(input("Enter the initial principal: "))
    years = int(input("Enter the number of years: "))
    FC = float(input("Enter the fixed contribution that will be made (beginning of period, not end): \n"))
    r = float(input("Enter the annual interest rate: ")) / 100
    n = float(input("Enter the number of annual compounding periods: "))

    print()
    print("Year      Value")
    print("-" * 17)

    for i in range(years + 1):
        t = i
        A = (FC * (((1 + (r / n)) ** (n * t) - 1) / (r / n)) * (1 + (r / n))) + (P * (1 + r / n) ** (n * t))
        A2 = round(A, 2)
        print("{:>3}     ${:0.2f}".format(str(i), A))

    print("The value in {} years is ${:,}".format(years, A2))

main()
