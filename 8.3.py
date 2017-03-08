def double(p):
    rate = 1 + (p/100)
    years = 0
    total = 1
    while total < 2:
        print("total is now", total)
        print("years is now", years)
        total *= rate
        years += 1
        print("total is now", total)
        print("years is now", years)
    return years

def main():
    print("\nThis app calculates how long it will take for an investment to double in value, given an interest rate.")
    p = float(input("\nEnter the interest rate: "))
    print("\nWith that rate of interest things will take {} years to double.".format(double(p)))
main()
