from math import pi
from graphics import *
from random import randrange

def main():
    printIntro()
    n, x, y = startup()
    printOutro(n, x, y)

def printIntro():
    print("\nThis app simulates 2D random walks with d4 rolls.")

def startup():
    win = mainWindow()
    #Cplane = cartPlane(win)
    n = getInput()
    posX, posY = drawRW(win, n)
    win.getMouse()
    win.close()
    return n, posX, posY


def mainWindow():
    # main window
    win = GraphWin("2D rectilinear random walk", 500, 500)
    win.setCoords(-60, -60, 60, 60)
    win.setBackground("gray")
    cartPlane(win)
    #O = Point(0, 0)
    #A = randomWalk(O)
    #L = Line(O, Point(10,0))
    #L.setFill("red")
    #L.draw(win)
    return win

def cartPlane(win):
    # Cartestian Plane
    Cplane = Rectangle(Point(-50, -50), Point(50, 50))
    Cplane.setFill("White")
    Cplane.draw(win)
    for i in range(10,100,10):
        L = 50
        V = Line(Point(i - L, -L), Point(i - L, L))
        V.setFill("gray")
        V.draw(win)
        H = Line(Point(-L, i - L), Point(L, i - L))
        H.setFill("gray")
        H.draw(win)
    return Cplane

def getInput():
    n = int(input("\nHow many rolls? "))
    return n

def drawRW(win, n):
    #import pdb; pdb.set_trace()
    print("I'm in drawRW now!")
    O = Point(0, 0)
    for i in range(n):
        print("I'm in the for loop now!")
        Ax, Ay = randomWalk(O)
        L = Line(Point(O.x, O.y), Point(Ax, Ay))
        L.setFill("red")
        L.draw(win)
        O.x, O.y = Ax, Ay
    return Ax, Ay

def randomWalk(P):
    print(P.x, P.y)
    d4_roll = randrange(4)
    print(d4_roll)
    if d4_roll == 0:
        P.x += 10
    elif d4_roll == 1:
        P.y += 10
    elif d4_roll == 2:
        P.x -= 10
    else:
        P.y -= 10
    print(P.x, P.y)
    return P.x, P.y

def printOutro(n, x, y):
    print("\nAfter {} rolls, you end up at ({}, {})\n".format(n, x, y))

if __name__ == '__main__':
    main()
