def main():

    print()

    print("This app finds the sum of the first n natural numbers,")
    print("with n defined by the user.")

    print()

    n = int(input("Please enter a whole number: "))
    Sum = 0
    for sums in range(n + 1):
        Sum = Sum + sums
    print()
    print("The sum of the first", n, "natural numbers is", Sum)
    print()

main()
