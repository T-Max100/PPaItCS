def main():

    name = input("Enter your name an I shall give you its value: ").lower()

    l = name.split()

    Jname = "".join(l)

    nameSum = 0

    for ch in Jname:
        nameSum = nameSum + ord(ch) - 96

    print("Your name sums to {0}".format(nameSum))

main()
