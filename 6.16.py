from graphics import *
#from math import *

def createWindow():
    win = GraphWin("Moving")
    win.setCoords(0,0,20,20)
    return win

def drawCircle(win):
    p = win.getMouse()
    c = Circle(p,2)
    c.setOutline("red")
    c.setFill("red")
    c.draw(win)
    return c


def moveTo(shape, newCenter):
    p = newCenter
    c = shape.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    shape.move(dx,dy)

def main():
    win = createWindow()
    shape = drawCircle(win)
    #newCenter = win.getMouse()
    #shape = Circle(newCenter, 20)

    for i in range(10):
        newCenter = win.getMouse()
        moveTo(shape, newCenter)


main()
