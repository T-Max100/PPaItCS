from graphics import *

from math import *

def main():
    win = GraphWin("Face")

    P = Point(100,100)

    c0 = Circle(P, 75)
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
    #P0.setOutline("purple")
    #P0.draw(win)

    R = Rectangle(P0, Point(P.getX() + (45*sin(pi/3)), P.getY() + 65*cos(pi/3)))
    R.setFill("yellow")
    R.setOutline("yellow")
    R.draw(win)

    win.getMouse()
    win.close()

main()
