from random import randrange

def main():
    printIntro()
    n = getInput()
    position = randomWalk(n)
    printOutro(n, position)

def printIntro():
    print("\nThis app simulates 1D random walks with coin flips.")

def getInput():
    n = int(input("\nHow many coin flips? "))
    return n
def randomWalk(n):
    x = 0
    for i in range(n):
        coin_flip = randrange(2)
        print(coin_flip)
        if coin_flip == 0:
            x += 1
        else:
            x -= 1
        print(x)
    return x

def printOutro(n, position):
    print("After {} coin flips, you end up at {}".format(n, position))

if __name__ == '__main__':
    main()
