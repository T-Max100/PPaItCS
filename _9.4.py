from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, noWin = simNGames(n, probA, probB)
    printSummary(winsA, winsB, noWin)

def printIntro():
    print("This program simulates a game of volleyball between two")
    print('players called "A" and "B".  The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of volleyball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = noWin = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB + 1:
            winsA += 1
        elif scoreB > scoreA + 1:
            winsB += 1
        else:
            noWin += 1
    return winsA, winsB, noWin

def simOneGame(probA, probB):
    # Simulates a single game or volleyball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                scoreB += 1
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                scoreA += 1
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return a==25 or b==25

def printSummary(winsA, winsB, noWin):
    # Prints a summary of wins for each player.
    n = winsA + winsB + noWin
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    print("Games not won: {0} ({1:0.1%})".format(noWin, noWin/n))

if __name__ == '__main__': main()
