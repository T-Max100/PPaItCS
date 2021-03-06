from graphics import *
from random import randrange

def main():
    printIntro()
    win = mainWindow()
    n, x, y = getInput(win)
    printOutro(n, x, y)

def printIntro():
    print("\nThis app simulates 2D random walks with d4 rolls.")

def mainWindow():
    win = GraphWin("2D rectilinear random walk", 500, 500)
    win.setCoords(-60, -60, 60, 60)
    win.setBackground("gray")
    cartPlane(win)
    return win

def cartPlane(win):
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

def getInput(win):
    n = int(input("\nHow many rolls? "))
    O = Point(0, 0)
    for i in range(n):
        A = Point(0, 0)
        A.x, A.y = randomWalk(Point(O.x, O.y))
        A = Point(A.x, A.y)
        L = Line(O, A)
        L.setFill("red")
        L.draw(win)
        O.x, O.y = A.x, A.y
    win.getMouse()

    return n, A.x, A.y

def randomWalk(P):
    d4_roll = randrange(4)
    if d4_roll == 0:
        P.x += 1
    elif d4_roll == 1:
        P.y += 1
    elif d4_roll == 2:
        P.x -= 1
    else:
        P.y -= 1
    return P.x, P.y

def printOutro(n, x, y):
    print("\nAfter {} rolls, you end up at ({}, {})\n".format(n, x, y))

if __name__ == '__main__':
    main()
