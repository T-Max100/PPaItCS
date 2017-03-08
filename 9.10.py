from random import random

def main():
    printIntro()
    n = getInputs()
    piApprox = simNThrows(n)
    printSummary(n, piApprox)

def printIntro():
    print("\nThis thing simulates throws of darts at a dart board.")
    print("It's doing this in order to approximate the constant Pi.")

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
    piApprox = 4 * (h / n)
    print(piApprox)
    return piApprox

def printSummary(n, piApprox):
    print("\nThe approximation of Pi after {} throws is {}".format(n, piApprox))

if __name__ == '__main__': main()
