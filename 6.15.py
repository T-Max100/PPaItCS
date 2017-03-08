from graphics import *
from math import *

def createWindow():
    win = GraphWin("Face", 800, 200)
    win.setCoords(0,0,20,5)
    return win

def drawFace(center, size, win):
    P = center
    x = P.getX
    y = P.getY

    # main disc
    c0 = Circle(P, size)
    c0.setFill("yellow")
    c0.draw(win)

    # left eye
    c1 = Circle(Point(P.getX() - (0.61*size*sin(pi/3)), P.getY() + 0.775*size*cos(pi/3)), size*.2)
    c1.setFill("white")
    c1.draw(win)

#   # right eye
    c2 = c1.clone()
    c2.move(1.22*size*sin(pi/3), 0)
    c2.draw(win)

    # main mouth
    O = Oval(Point(P.getX() - (0.61*size*sin(pi/3)), P.getY() - 0.375*size*cos(pi/3)), Point(P.getX() + (0.61*size*sin(pi/3)), P.getY() - 1.25*size*cos(pi/3)))
    O.setFill("yellow")
    O.draw(win)

    P0 = Point(P.getX() - (0.61*size*sin(pi/3)), P.getY() - 0.375*size*cos(pi/3))

    # finish mouth
    R = Rectangle(P0, Point(P.getX() + (0.61*size*sin(pi/3)), P.getY() - 0.8125*size*cos(pi/3)))
    R.setFill("yellow")
    R.setOutline("yellow")
    R.draw(win)

def main():
    X = [1.5, 5, 10, 17]

    win = createWindow()

    scale = 0.5
    size = 1

    for x in X:
        P = Point(x, 2.5)
        drawFace(P, size, win)
        size += scale

    win.getMouse()
    win.close()
main()
