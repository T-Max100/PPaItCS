def main():

    phrase = input("Enter a phrase you want an acronym for: ")

    Sphrase = phrase.split()

    ac = ""

    for w in Sphrase:
        ac = ac + w[0]

    print("The acronym is {0}".format(ac.upper()))

main()
