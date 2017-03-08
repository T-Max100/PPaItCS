from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(0,25), Point(25,0))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape = shape.clone()
        shape.move(dx,dy)
        shape.draw(win)
    Text(Point(100,100), "Click again to quit!").draw(win)
    win.getMouse()
    win.close()
main()
