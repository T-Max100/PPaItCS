from graphics import *
from button import Button

def createLabeledWindow():
    window = GraphWin("Draw a Regression Line", 600, 600)
    window.setCoords(0.0, 0.0, 6.0, 6.0)
    greet(window)
    return window

def greet(window):
    message = Text(Point(3, 0.3), "Click on some points")
    message.draw(window)
    window.getMouse()
    message.undraw()

def drawPoints(window):
    SumX = 0
    SumY = 0
    SumXX = 0
    SumXY = 0
    lx = []
    ly = []
    p = window.getMouse()
    while (p.getX() >= 1) or (p.getY() >= 0.5):
        p.setFill("blue")
        p.draw(window)
        lx.append(p.getX())
        ly.append(p.getY())
        SumX += p.getX()
        SumY += p.getY()
        SumXX += p.getX() * p.getX()
        SumXY += p.getX() * p.getY()
        p = window.getMouse()
    print(lx, ly)
    print(len(lx), len(ly))
    n = len(lx)
    print("SumX is {:0.3f}, SumY is {:0.3f}, SumXX is {:0.3f}, SumXY is {:0.3f}".format(SumX, SumY, SumXX, SumXY))
    return SumX, SumY, SumXX, SumXY, n

def slopeCalc(SumX, SumY, SumXX, SumXY, n):
    m = (n * SumXY - SumX * SumY) / (n * SumXX - SumX * SumX)
    return m

def yCalc(SumX, SumY, m, n, window):
    y1 = (SumY / n) + m * (0 - SumX / n)
    y2 = (SumY / n) + m * (6 - SumX / n)
    drawRegLine(y1, y2, window)

def drawRegLine(y1, y2, window):
    R = Line(Point(0, y1), Point(6, y2))
    R.setFill("red")
    R.draw(window)

def main():
    print("\nThis app graphically plots a regression line")
    win = createLabeledWindow()
    done_close = Button(win, Point(0.5, 0.25), 1, 0.5, "Done")
    done_close.activate()
    SumX, SumY, SumXX, SumXY, n = drawPoints(win)
    m = slopeCalc(SumX, SumY, SumXX, SumXY, n)
    yCalc(SumX, SumY, m, n, win)

    done_close.changeText(win, Point(0.5, 0.25), "Close")
    done_close.deactivate()
    win.getMouse()

main()
