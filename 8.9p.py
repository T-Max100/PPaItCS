def main():
    print('Multi-leg Journey\'s fuel efficiency calculator.\n')

    try:
        # Get starting point of odometer
        # No data validate since you need to check possible of Empty String enter
        while True:
            oStart = input('What\'s status of starting odometer: ')

            if oStart == '': oStart = 0

            # THIS GO ERROR IF ITS NOT STRING NUMBER!!
            oStart = float(oStart)

            if oStart < 0:
                    print('Error, correct your odometer.\n')
            else:
                break

        # keep oStart to calculate Total MPG for all trip
        oLast = oStart
        gLast = 0
        legCount = 1
        legMPG = []

        # Now collect all detail of each leg
        # Sentinel Loop pattern
        raw = input('\nLeg #{}, What\'s odometer status now? and  how much gas been used?\n\
Please separate each data by space [Odometer Gas]:'.format(legCount))

        while raw !='':

            oTotal,gTotal = raw.split()
            oTotal = float(oTotal)
            gTotal = float(gTotal)

            legMPG.append(round((oTotal-oLast)/(gTotal-gLast),1))

            oLast = oTotal
            gLast = gTotal

            legCount = legCount+1

            raw = input('\nLeg #{}, What\'s odometer status now? and  how much gas been used?\n\
Please separate each data by space [Odometer Gas]:'.format(legCount))


        if legCount > 1:
            print('\nYour fuel efficiency are:')

            # at this point legCount must be at least 1
            for i in range(legCount-1):
                print('Leg#{} has {} MPG.'.format(i+1,legMPG[i]))

            #when trip end calculate total MpG of whole trip
            print('\nYour total MPG is',round((oTotal-oStart)/gTotal,2))
        else:
            print('\nNo result.')

    except ValueError:
        print('\nPlease correct your input.')
    except:
        print('\nUnknow Error! Please try again.')

if __name__ =='__main__': main()
