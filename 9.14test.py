from graphics import *
from random import randrange

def main():
    win = GraphWin("2D rectilinear random walk", 500, 500)
    win.setCoords(-60, -60, 60, 60)
    win.setBackground("gray")
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

    O = Point(0, 0)
    n = int(input("\nHow many rolls? "))
    for i in range(n):
        A = Point(0, 0)
        A.x, A.y = randomWalk(Point(O.x, O.y))
        A = Point(A.x, A.y)
        L = Line(O, A)
        L.setFill("red")
        L.draw(win)
        O.x, O.y = A.x, A.y

    win.getMouse()
    win.close()

def randomWalk(P):
    #print(P.x, P.y)
    d4_roll = randrange(4)
    #print(d4_roll)
    if d4_roll == 0:
        P.x += 1
    elif d4_roll == 1:
        P.y += 1
    elif d4_roll == 2:
        P.x -= 1
    else:
        P.y -= 1
    #print(P.x, P.y)
    return P.x, P.y

if __name__ == '__main__':
    main()
