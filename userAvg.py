def main():

    print()

    print("This will average numbers you provide!")

    print()

    n = int(input("How many nummbers will you be averaging?: "))

    avg = 0

    print()

    for num in range(n):
        number = int(input("Enter number: "))
        avg = avg + number

    avg = avg / n

    print("The average of those numbers is", avg)

    print()

main()
