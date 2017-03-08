def overtimeCalc(hours, rate):
    base = 40 * rate
    over = hours - 40
    pay = base + over * rate * 1.5
    return pay

def main():
    print()
    print("This app calculates weekly wages, assuming overtime is paid at\ntime-and-a-half.\n")
    H = float(input("How many hours total were worked this week?: "))
    R = float(input("What's the hourly salary rate?: "))
    print("Your pay for the week is ${:0.2f}\n".format(overtimeCalc(H, R)))
main()
