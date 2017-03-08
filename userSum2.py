def main():

    print()

    print("This will add up numbers you provide!")

    print()

    n = int(input("How many nummbers will you be adding together?: "))

    Sum = 0

    print()

    for num in range(n):
        number = int(input("Enter number: "))
        Sum = Sum + number

    print("The sum of those numbers is", Sum)

    print()

main()
