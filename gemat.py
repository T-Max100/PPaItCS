def main():

    name = input("Enter your name an I shall give you its value: ").lower()

    l = []

    nameSum = 0

    for ch in name:
        #l.append(ch)
        nameSum = nameSum + ord(ch) - 96

    print("Your name sums to {0}".format(nameSum))

main()
