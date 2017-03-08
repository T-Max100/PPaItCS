from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, ralWinsA, ralWinsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, ralWinsA, ralWinsB)

def printIntro():
    print("This program simulates a game of tennis between two")
    print('players called "A" and "B".  The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = winsB = 0
    ralWinsA = ralWinsB = 0
    for i in range(n):
        scoreA, scoreB, ralScoreA, ralScoreB = simOneGame(probA, probB, i)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
        if ralScoreA > ralScoreB:
            ralWinsA += 1
        else:
            ralWinsB += 1
    return winsA, winsB, ralWinsA, ralWinsB

def simOneGame(probA, probB, i):
    if i % 2 == 0:
        serving = "A"
    else:
        serving = "B"
    scoreA = scoreB = 0
    ralScoreA = ralScoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
                ralScoreA += 1
            else:
                ralScoreB += 1
                #serving = "B"
        else:
            if random() < probB:
                scoreB += 1
                ralScoreB += 1
            else:
                ralScoreA += 1
                #serving = "A"
    return scoreA, scoreB, ralScoreA, ralScoreB

def gameOver(a, b):
    return a >= 4 and b <= a - 2 or b >= 4 and a <= b - 2

def printSummary(winsA, winsB, ralWinsA, ralWinsB):
    n = winsA + winsB
    nRal = ralWinsA + ralWinsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    print("Rally wins for A: {0} ({1:0.1%})".format(ralWinsA, ralWinsA/nRal))
    print("Rally wins for B: {0} ({1:0.1%})".format(ralWinsB, ralWinsB/nRal))

if __name__ == '__main__': main()

# This file should also be considered the basis for a better version 9.3 and 9.4.
