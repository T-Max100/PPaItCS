from random import randint

def main():
    printIntro()
    n = getInputs()
    estimation = process(n)
    finish(estimation)

def printIntro():
    print("\nThis app simulates craps games.")

def getInputs():
    n = int(input("\nHow many games do you want to simulate? "))
    return n

def process(n):
    wins = 0
    for i in range(n):
        if singleCrapsToss() == True:
            wins += 1
    return wins/n

def singleCrapsToss():
    nextToss, count = 0, 0
    game0 = randint(1, 12)
    if game0 in (2, 3, 12):
        return False
    elif game0 in (7, 11):
        return True
    else:
        nextToss = randint(1,12)
        while nextToss not in (game0, 7):
            nextToss = randint(1,12)
            count += 1
        #print(count)
        if nextToss == 7:
            return False
        elif nextToss == game0:
            return True

def finish(estimation):
    print("\nYour estimated probability of winning is {}. Which is {}‰ or {}%.".format(estimation, estimation*1000, estimation*100))
if __name__ == '__main__': main()

# potential redesign. Could use the strings "win" and "lose" instead of bools. Could create function playForPoint(game0) that incorporates the else branch here. I'm just going to make it in a jupyter notebook.
