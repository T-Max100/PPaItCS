def main():

    print()

    print("This will add up numbers you provide!")

    print()

    l = list(eval(input("Enter your numbers separated by commas: ")))

    Sum = 0

    print()

    for num in l:
        Sum = Sum + num

    print("The sum of those numbers is", Sum)

    print()

main()
