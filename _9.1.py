from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, bestOf = simNGames(n, probA, probB)
    printSummary(n, winsA, winsB, bestOf)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B".  The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A and")
    print("Player B alternate in serving.")

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    #import ipdb; ipdb.set_trace()
    # Simulates best of n games of racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    if n % 2 == 0:
        bestOf = n/2 + 1
    else:
        bestOf = (n + 1)/2
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, i)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
        if bestOf in [winsA, winsB]:
            break
    return winsA, winsB, bestOf

def simOneGame(probA, probB, i):
    # Simulates a single game or racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    if i % 2 != 0:
        serving = "A"
    else:
        serving = "B"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a==15 or b==15

def printSummary(n, winsA, winsB, bestOf):
    # Prints a summary of wins for each player.
    played = winsA + winsB
    print("\nGames played:", played)
    print("{} wins was the best of {} games".format(bestOf, n))
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/played))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/played))

if __name__ == '__main__': main()
