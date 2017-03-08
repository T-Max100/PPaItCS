from graphics import *

def main():
    win = GraphWin("Dice", 500, 100)
    win.setCoords(0.0, 0.0, 10.0, 2.0)

    s0 = Rectangle(Point(0.5, 0.5), Point(1.5, 1.5))
    s0.setFill("red")
    s0.draw(win)

    s1 = s0.clone()
    s1.move(2.0, 0)
    s1.draw(win)

    s2 = s0.clone()
    s2.move(4.0, 0)
    s2.draw(win)

    s3 = s0.clone()
    s3.move(6.0, 0)
    s3.draw(win)

    s4 = s0.clone()
    s4.move(8.0, 0)
    s4.draw(win)

    d0 = Circle(Point(1, 1), 0.1)
    d0.setFill("white")
    d0.draw(win)

    d1 = d0.clone()
    d1.move(1.7, 0.3)
    d1.draw(win)

    d2 = d0.clone()
    d2.move(2.3, -0.3)
    d2.draw(win)

    d3 = d0.clone()
    d3.move(4.0, 0)
    d3.draw(win)

    d4 = d0.clone()
    d4.move(3.7, 0.3)
    d4.draw(win)

    d5 = d0.clone()
    d5.move(4.3, -0.3)
    d5.draw(win)

    d6 = d0.clone()
    d6.move(5.7, 0.3)
    d6.draw(win)

    d7 = d0.clone()
    d7.move(6.3, -0.3)
    d7.draw(win)

    d8 = d0.clone()
    d8.move(6.3, 0.3)
    d8.draw(win)

    d9 = d0.clone()
    d9.move(5.7, -0.3)
    d9.draw(win)

    d10 = d0.clone()
    d10.move(8.0, 0)
    d10.draw(win)

    d11 = d0.clone()
    d11.move(7.7, 0.3)
    d11.draw(win)

    d12 = d0.clone()
    d12.move(8.3, -0.3)
    d12.draw(win)

    d13 = d0.clone()
    d13.move(8.3, 0.3)
    d13.draw(win)

    d14 = d0.clone()
    d14.move(7.7, -0.3)
    d14.draw(win)

    win.getMouse()
    win.close()

main()
