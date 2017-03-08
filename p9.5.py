from random import random
from IPython.core.debugger import Tracer

def main():
    printIntro()
    probA, probB = getInputs()

    # I force 1000 games to make result usable because if let user enter very close
    # prob like A=0.7, B=0.69 then you can not compare anything it just too random
    games = 1000

    winsAreg, winsBreg, winsAral, winsBral = simNGames(probA, probB, games)

    comment = getComment(winsAreg, winsBreg, winsAral,
                          winsBral, probA, probB, games)

    printSummary(winsAreg, winsBreg, winsAral, winsBral,
                 games, comment)


def printIntro():
    print(
'''A Program to simulate two type of volleyball systems.
Result of 1000 games between regular type and rally scoring type
will be compare and print summary at the end of process.\n
Please provide different probability for each team.
====================================================''')


def getInputs():

    #Use loop here to validate prob of both team must different
    #or the end result is just too random.
    while True:
        a = eval(input('\nWhat is the prob. team A wins a serve? '))
        b = eval(input('What is the prob. team B wins a serve? '))

        if a == b: print('\nERROR! Each team must have different probability! Try again!')
        else: break

    return a,b


def simNGames(probA,probB,games):
    winsAreg = winsBreg = 0 # present regular type
    winsAral = winsBral = 0 # present rally scoring type

    for i in range(games):

        #swap serving each game
        if i%2 == 0: serving = 'A'
        else: serving = 'B'

        # REGULAR GAME #
        scoreA, scoreB = simOneGame(probA,probB,serving,'regular')

        if scoreA > scoreB:
            winsAreg = winsAreg + 1
        else:
            winsBreg = winsBreg + 1

        # RALLY GAME #
        scoreA, scoreB = simOneGame(probA,probB,serving,'rally')

        if scoreA > scoreB:
            winsAral = winsAral + 1
        else:
            winsBral = winsBral + 1

    return winsAreg, winsBreg, winsAral, winsBral,


def simOneGame(probA,probB,serving,type):
    #Tracer()()
    scoreA = scoreB = 0
    r = random()

    # REGULAR GAME #
    if type == 'regular':

        while not gameOver(scoreA,scoreB,type):

            if serving =='A':
                if r < probA:
                    scoreA = scoreA + 1
                else:
                    serving = 'B'
            else:
                if r < probB:
                    scoreB = scoreB + 1
                else:
                    serving = 'A'

    # RALLY GAME #
    if type == 'rally':

        while not gameOver(scoreA,scoreB,type):

            if serving =='A':
                if  r < probA:
                    scoreA = scoreA + 1
                else:
                    scoreB = scoreB + 1
                    serving = 'B'
            else:
                if r < probB:
                    scoreB = scoreB + 1
                else:
                    scoreA = scoreA + 1
                    serving = 'A'

    return scoreA, scoreB


def gameOver(a,b,type):

    if type == 'regular':
        #won by 15 + margin of 2
        status = ((a >= 15) and (a-b >= 2)) or ((b >= 15) and (b-a >= 2))

    if type == 'rally':
        #won by 25 + margin of 2
        status = ((a >= 25) and (a-b >= 2)) or ((b >= 25) and (b-a >= 2))

    return status


def getComment(winsAreg, winsBreg, winsAral, winsBral, probA, probB, games):

    # check if teamA or teamB is has better probability
    # then calculate are they won more or less from rally scoring type

    if probA == max(probA,probB):

        betterteam = 'A'
        diff = (winsAral-winsAreg)/games

    else:

        betterteam = 'B'
        diff = (winsBral-winsBreg)/games

    return genComment(betterteam,diff)


def genComment(betterteam,diff):

    # finally generate comment text to use at end result
    if diff > 0:
        c ='Conclusion:\nTeam {0} is better team and enjoy benefit {1:0.1%} from rally scoring system.'.format(betterteam,diff)

    elif diff < 0:
        c ='Conclusion:\nEven Team {0} is a better but their advantage is reduce {1:0.1%} by rally scoring system.'.format(betterteam,diff)

    else:
        c ='Conclusion:\nTeam {0} is better but does not gain benefit from rally scoring system.'.format(betterteam)

    return c


def printSummary(winsAreg,winsBreg,winsAral,winsBral,games,comment):

    print('\nGames simulated:',games)

    print('\nRegular type games result:')
    print('Wins for A: {0} ({1:0.1%})'.format(winsAreg, winsAreg/games))
    print('Wins for B: {0} ({1:0.1%})'.format(winsBreg, winsBreg/games))

    print('\nRally Scoring type games result:')
    print('Wins for A: {0} ({1:0.1%})'.format(winsAral, winsAral/games))
    print('Wins for B: {0} ({1:0.1%})'.format(winsBral, winsBral/games))

    print('\n====================================================')
    print(comment)

if __name__ == '__main__' : main()
