from graphics import *

def main():

    # Creating window, title bar, and coordinate system
    win = GraphWin("Five-click house", 500, 500)
    win.setCoords(0, 0, 500, 500)

    # Getting points from clicks and making initial rectangle
    c0 = win.getMouse()
    #c0.draw(win)
    c1 = win.getMouse()
    #c1.draw(win)
    r = Rectangle(c0, c1)
    r.draw(win)

    # Getting the top center of the door and tf. width
    dx = abs(c0.getX() - c1.getX())
    c2 = win.getMouse()
    c3 = c2.clone()
    c3.move(dx / 10, 0)
    c4 = c2.clone()
    c4.move(-dx / 10, 0)

    # Drawing the door
    l0 = Line(c3, c4)
    l0.draw(win)
    l1 = Line(c3, Point(c3.getX(), c0.getY()))
    l1.draw(win)
    l2 = Line(c4, Point(c4.getX(), c0.getY()))
    l2.draw(win)

    # Getting window points
    c5 = win.getMouse()
    c6 = c5.clone()
    c6.move(dx / 20, dx /20)
    c7 = c5.clone()
    c7.move(-dx / 20, dx /20)
    c8 = c5.clone()
    c8.move(dx / 20, -dx /20)
    c9 = c5.clone()
    c9.move(-dx / 20, -dx /20)

    # Drawing window
    l3 = Line(c6, c7)
    l3.draw(win)
    l4 = Line(c7, c9)
    l4.draw(win)
    l5 = Line(c9, c8)
    l5.draw(win)
    l6 = Line(c8, c6)
    l6.draw(win)

    # Getting point for roof peak and drawing roof
    c10 = win.getMouse()
    t = Polygon(Point(c0.getX(),c1.getY()), c1, c10)
    t.draw(win)

    win.getMouse()
    win.close()

main()
