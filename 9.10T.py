from random import random

def main():
    printIntro()
    n = getInputs()
    tauApprox = simNThrows(n)
    printSummary(n, tauApprox)

def printIntro():
    print("\nThis thing simulates throws of darts at a dart board.")
    print("It's doing this in order to approximate the constant Tau.")

def getInputs():
    n = int(input("\nHow many darts should be thrown? "))
    return n

def simNThrows(n):
    h = 0
    for i in range(n):
        x = 2 * random() - 1
        y = 2 * random() - 1
        #print(x, y)
        if x ** 2 + y ** 2 <= 1:
            h += 1
    print(h)
    tauApprox = 8 * (h / n)
    print(tauApprox)
    return tauApprox

def printSummary(n, tauApprox):
    print("\nThe approximation of Tau after {} throws is {}\n".format(n, tauApprox))

if __name__ == '__main__': main()
