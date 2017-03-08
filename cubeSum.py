def main():

    print()

    print("This app finds the sum of the cubes of the first n natural")
    print("numbers, with n defined by the user.")

    print()

    n = int(input("Please enter a whole number: "))
    Sum = 0
    for sums in range(n + 1):
        Sum = Sum + sums ** 3
    print()
    print("The sum of the first", n, "natural numbers cubed is", Sum)
    print()

main()
