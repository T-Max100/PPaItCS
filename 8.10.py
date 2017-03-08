def eff(l, f):
    line = f.readline()
    leg = 0
    lmpg = []
    t = 0
    entries = line
    while True:
        odo, gal = entries.split()
        odo, gal = float(odo), float(gal)
        l[0], l[1] = odo + l[0], gal + l[1]
        MPG = odo / gal
        leg += 1
        lmpg.append(MPG)
        line = f.readline()
        entries = line
        if (entries == ''):
            print(l[0], l[1])
            for r in lmpg:
                t += r
            for i in range(leg):
                print("\nThe fuel economy of leg {} in MPG is {:.0f}\n".format(i+1, lmpg[i]))
            print("\nThe total MPG for the whole trip is {:.0f}\n".format(l[0] / l[1]))
            break

def main():
    print("\nThis app computes fuel efficiency")
    fileName = input("What file are the entries in? ")
    infile = open(fileName, 'r')
    line = infile.readline()
    odo = line
    l = [float(odo), 0]
    eff(l, infile)
main()
