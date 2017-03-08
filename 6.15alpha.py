from graphics import *
from math import *

def createWindow():
    win = GraphWin("Face", 800, 200)
    return win

def drawFace(center, size, win):
    P = center
    c0 = Circle(P, size)
    c0.setFill("yellow")
    c0.draw(win)

    c1 = Circle(Point(P.getX() - (45*sin(pi/3)), P.getY() - 45*cos(pi/3)), 15)
    c1.setFill("white")
    c1.draw(win)

    c2 = c1.clone()
    c2.move(90*sin(pi/3), 0)
    c2.draw(win)

    O = Oval(Point(P.getX() - (45*sin(pi/3)), P.getY() + 30*cos(pi/3)), Point(P.getX() + (45*sin(pi/3)), P.getY() + 100*cos(pi/3)))
    O.setFill("yellow")
    O.draw(win)

    P0 = Point(P.getX() - (45*sin(pi/3)), P.getY() + 30*cos(pi/3))

    R = Rectangle(P0, Point(P.getX() + (45*sin(pi/3)), P.getY() + 65*cos(pi/3)))
    R.setFill("yellow")
    R.setOutline("yellow")
    R.draw(win)

    win.getMouse()
    win.close()

def main():
    P = Point(100,100)
    win = createWindow()
    drawFace(P, 75, win)
main()
