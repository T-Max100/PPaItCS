from random import randrange

def main():
    printIntro()
    n = getInput()
    position = randomWalk(n)
    printOutro(n, position)

def printIntro():
    print("\nThis app simulates 2D random walks with d4 rolls.")

def getInput():
    n = int(input("\nHow many rolls? "))
    return n

def randomWalk(n):
    x = [0, 0]
    for i in range(n):
        d4_roll = randrange(4)
        print(d4_roll)
        if d4_roll == 0:
            x[0] += 1
        elif d4_roll == 1:
            x[1] += 1
        elif d4_roll == 2:
            x[0] -= 1
        else:
            x[1] -= 1
        #print(x)
    return x

def printOutro(n, position):
    print("\nAfter {} rolls, you end up at {}\n".format(n, position))

if __name__ == '__main__':
    main()
