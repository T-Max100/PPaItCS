from graphics import *

def main():

    win = GraphWin("Winter Scene", 400, 400)
    win.setBackground(color_rgb(192,240,255))
    win.setCoords(0.0, 0.0, 4.0, 4.0)

    o = Oval(Point(-1.5, 1.5), Point(5.5, -2.0))
    o.setFill("white")
    o.setOutline("white")
    o.draw(win)

    c0 = Circle(Point(3.0, 1.5), 0.5)
    c0.setFill("white")
    c0.draw(win)

    c1 = Circle(Point(3.0, 2.0), 0.4)
    c1.setFill("white")
    c1.draw(win)

    c2 = Circle(Point(3.0, 2.5), 0.3)
    c2.setFill("white")
    c2.draw(win)

    R = Rectangle(Point(0.5, 1.0), Point(0.75, 1.5))
    R.setFill("brown")
    R.draw(win)

    T0 = Polygon(Point(0.0, 1.5), Point(1.25, 1.5), Point(0.625, 2.125))
    T0.setFill(color_rgb(0,192,64))
    T0.draw(win)

    T1 = Polygon(Point(0.125, 1.8125), Point(1.125, 1.8125), Point(0.625, 2.3625))
    T1.setFill(color_rgb(0,192,64))
    T1.draw(win)

    T2 = Polygon(Point(0.25, 2.125), Point(1.0, 2.125), Point(0.625, 2.6))
    T2.setFill(color_rgb(0,192,64))
    T2.draw(win)

    win.getMouse()
    win.close()

main()
