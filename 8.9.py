def eff(l):
    leg = 0
    lmpg = []
    t = 0
    entries = input("\nEnter the current odometer reading and the amount of gas used (separated by a space): ")
    while True:
        odo, gal = entries.split()
        odo = float(odo)
        gal = float(gal)
        dist = odo - l[0]
        l[0], l[1] = odo, l[1] - gal
        MPG = dist / gal
        leg += 1
        lmpg.append(MPG)
        entries = input("\nEnter the current odometer reading and the amount of gas used (separated by a space): ")
        if (entries == ''):
            for r in lmpg:
                t += r
            for i in range(leg):
                print("\nThe fuel economy of leg {} in MPG is {:.0f}\n".format(i+1, lmpg[i]))
            print("\nThe total MPG for the whole trip is {:.0f}\n".format(t / len(lmpg)))
            break

def main():
    print("\nThis app computes fuel efficiency")
    odo = float(input("\nWhat's the starting odometer reading?: "))
    #gal = float(input("\nHow many gallons of gas will fill the tank?: "))
    #l = [odo, gal]
    l = [odo, 0]
    eff(l)
main()
