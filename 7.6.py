def fineCalc(limit, speed):
    exc = speed - limit
    if speed > 90:
        fine = 50 + 5 * exc + 200
        print("Your fine is ${:.2f}!".format(fine))
    elif limit <= speed <= 90:
        fine = 50 + 5 * exc
        print("Your fine is ${:.2f}!".format(fine))
    elif speed <= limit:
        print("You're free of the beast… this time.")

def main():
    print()
    print("This app calculates your speeding ticket if you were speeding.\n")
    print()
    L, S = eval(input("What's the speed limit and the speed of travel?: "))
    print()
    fineCalc(L, S)
main()
