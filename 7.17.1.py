from graphics import *

def createWindow():
    win = GraphWin("Moving", 900, 300)
    win.setCoords(-15,-5,15,5)
    return win

def drawCircle(win):
    p = win.getMouse()
    r = 1
    #p = Point(0, 0)
    c = Circle(p,r)
    c.setOutline("red")
    c.setFill("red")
    c.draw(win)
    return c

def moveRightLeft(x, dx):
    if x >= 14:
        dx = -1
    if x <= -14:
        dx = 1
    return dx

def moveUpDown(y, dy):
    if y >= 4:
        dy = -1
    if y <= -4:
        dy = 1
    return dy

def main():
    win = createWindow()
    shape = drawCircle(win)

    dx, dy = 1, 1

    for i in range(400):
        posA = shape.getCenter().getX()
        pos1 = shape.getCenter().getY()
        dx = moveRightLeft(posA, dx)
        dy = moveUpDown(pos1, dy)

        shape.move(dx,dy)

    win.getMouse()
    win.close()
main()
