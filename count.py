def main():

    print()

    print("This program counts lines, words, and characters in a file.")

    infileDoc = input("What file should be counted up?: ")
    print()

    infile = open(infileDoc, "r")

    lc, wc, cc = 0, 0, 0

    for line in infile:
        #print(line)
        lc = lc + 1
        #print(line.split())
        wc = wc + len(line.split())
        #print(wc)
        cc = cc + len(line[:-1])
        #print(cc)

    infile.close()

    print("L:{} W:{} C:{}".format(lc, wc, cc))

main()
