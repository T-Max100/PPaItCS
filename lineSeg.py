from graphics import *

def main():

    # Create the window
    win = GraphWin("Line Segment Information", 1000, 1000)
    win.setCoords(0, 0, 1000, 1000)

    # Explain to user what the app does
    intro = Text(Point(250, 975), "This app will draw a line segment between two mouse clicks and show some info about it.")
    intro.draw(win)

    # Get points from mouse clicks
    p0 = win.getMouse()
    p0.draw(win)
    p1 = win.getMouse()
    p1.draw(win)

    # Create line
    l = Line(p0, p1)
    l.draw(win)

    # Find midpoint of line
    mid = Point(((p0.getX() + p1.getX()) / 2),((p0.getY() + p1.getY()) / 2))
    mid.setFill("cyan")
    mid.draw(win)
    print(mid.getX(), mid.getY())

    # Getting the slope of the line
    dx = p0.getX() - p1.getX()
    dy = p0.getY() - p1.getY()
    m = dy / dx
    print("This line's slope is",m)

    # Getting the line's length
    s = (dx ** 2 + dy ** 2) ** 0.5
    print("This line's length is", s)

    win.getMouse()
    win.close()

main()
