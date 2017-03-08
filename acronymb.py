def main():

    print("This program creates a file of acronyms from a")
    print("file of phrases.")

    infilePhrase = input("What file are the phrases in?: ")
    outfilePhrase = input("What file do the acronyms go in?: ")

    infile = open(infilePhrase, "r")
    outfile = open(outfilePhrase, "w")

    for phrase in infile:
        Sphrase = phrase.split()
        ac = ""
        for w in Sphrase:
            ac = ac + w[0]
        UAC = ac.upper()
        print("The acronym is {0}".format(UAC))
        print(UAC, file = outfile)

    infile.close()
    outfile.close()

    print("Acronyms have been written to", outfilePhrase)

main()
