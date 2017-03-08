def main():

    s = input("Enter a string of words: ")

    j = "".join(s.split())

    print("The average word length is {}".format(len(j)/len(s.split())))
    print("Which is about {}".format(round(len(j)/len(s.split()))))

main()
