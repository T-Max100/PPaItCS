from graphics import *
#from math import *

def createWindow():
    win = GraphWin("Moving", 900, 300)
    win.setCoords(-15,-5,15,5)
    return win

def drawCircle(win):
    #p = win.getMouse()
    r = 1
    p = Point(0, 0)
    c = Circle(p,r)
    c.setOutline("red")
    c.setFill("red")
    c.draw(win)
    return c


#def moveTo(shape):
#    #p = newCenter
#    c = shape.getCenter()
#    print("X", c.getX())
#    print("Y", c.getY())
#    #dx = 1
#    #dy = 1
#
#    if 323 <= c.getX() <= 325:
#        print("(A) activated")
#        dx = -1
#        if 323 <= c.getY() <= 325:
#            print("(A.1) activated")
#            dy = -1
#    elif -324 <= c.getX() <= -323:
#        print("(B) activated")
#        dx = -1
#        if -324 <= c.getY() <= -323:
#            print("(B.1) activated")
#            dy = -1
#    else:
#        print("(D) activated")
#        dx = 1
#        dy = 1
#
#    shape.move(dx,dy)

"""
def moveUpDown(shape, D, E):
    c = shape.getCenter()
    dx = 1
    print("X", c.getX())
    if 324 <= c.getX():
        if E == 1:
            dx = -1
        elif E == -1:
            dx = -1
    #elif 324 >= c.getX():
    #    if E == 1:
    #        dx = 1
    #    elif E == -1:
    #        dx = -1

    if -324 >= c.getX():
        if E == -1:
            dx = 1
        elif E == 1:
            dx = 1
    #elif -324 <= c.getX():
    #    if E == 1:
    #        dx = 1
    #    elif E == -1:
    #        dx = -1
    print("dx is", dx)
    return dx
"""

"""
def moveRightLeft(shape, D, E):
    c = shape.getCenter()
    dy = 1
    print("Y", c.getY())
    if 324 <= c.getX() and D == 1:
        dy = -1
    elif 324 >= c.getY() and E == -1:
        dy = -1

    if -324 >= c.getY() and D == -1:
        dy = 1
    elif -324 <= c.getY() and E == 1:
        dy = 1
    print("dy is", dy)
    return dy
"""
"""
def moveRightLeft(shape, D, E):
    c = shape.getCenter()
    dy = 1
    print("Y", c.getY())
    if 324 <= c.getY():
        if E == 1:
            dy = -1
        elif E == -1:
            dy = -1
    #elif 324 >= c.getY():
    #    if E == 1:
    #        dy = 1
    #    elif E == -1:
    #        dy = -1

    if -324 >= c.getY():
        if E == -1:
            dy = 1
        elif E == 1:
            dy = 1
    #elif -324 <= c.getY():
    #    if E == 1:
    #        dy = 1
    #    elif E == -1:
    #        dy = -1
    print("dy is", dy)
    return dy
"""

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

"""
def moveTo(shape, D, E):
    dx = moveUpDown(shape, D, E)
    dy = moveRightLeft(shape, D, E)
    shape.move(dx, dy)
"""

def main():
    win = createWindow()
    shape = drawCircle(win)
    #posA = shape.getCenter().getX()
    #posB = 0
    #pos1 = shape.getCenter().getY()
    #pos2 = 0
    #newCenter = win.getMouse()
    #shape = Circle(newCenter, 20)
    """win = GraphWin("Moving", 720, 720)
    win.setCoords(-360,-360,360,360)

    p = Point(0, 0)
    shape = Circle(p,36)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)"""

    dx, dy = 1, 1

    """for i in range(1200):
        #newCenter = win.getMouse()
        D = posB - posA
        E = pos2 - pos1
        print("posB - posA = D equates to {} - {} = {}".format(posB, posA, D))
        print("pos2 - pos1 = E equates to {} - {} = {}".format(pos2, pos1, E))
        print("D is {}, E is {}".format(D, E))
        moveTo(shape, D, E)
        print("posA is now", posA)
        print("posB is now", posB)
        print("pos1 is now", pos1)
        print("pos2 is now", pos2)
        print("D is {}, E is {}".format(D, E))
        posA, pos1 = posB, pos2
        print("posA is now", posA)
        print("posB is now", posB)
        print("pos1 is now", pos1)
        print("pos2 is now", pos2)
        print("D is {}, E is {}".format(D, E))
        posB, pos2 = shape.getCenter().getX(), shape.getCenter().getY()
        print("D is {}, E is {}".format(D, E))
        print("posB - posA = D equates to {} - {} = {}".format(posB, posA, D))
        print("D is {}, E is {}".format(D, E))
        print("pos2 - pos1 = E equates to {} - {} = {}".format(pos2, pos1, E))
        print("D is {}, E is {}".format(D, E))"""
    """for i in range(400):
        #posA = shape.getCenter().getX()
        #pos1 = shape.getCenter().getY()
        c = shape.getCenter()
        if c.getX() >= 324:
            dx = -1
        if c.getX() <= -324:
            dx = 1
        if c.getY() >= 324:
            dy = -1
        if c.getY() <= -324:
            dy = 1
        shape.move(dx,dy)"""

    for i in range(400):
        posA = shape.getCenter().getX()
        pos1 = shape.getCenter().getY()
        dx = moveRightLeft(posA, dx)
        dy = moveUpDown(pos1, dy)

        shape.move(dx,dy)

    win.getMouse()
    win.close()
main()
