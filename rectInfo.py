from graphics import *

def main():

    # Create the window
    win = GraphWin("Line Segment Information", 1000, 1000)
    win.setCoords(0, 0, 1000, 1000)

    # Explain to user what the app does
    intro = Text(Point(250, 975), "This app will draw a rectangle between two mouse clicks and give some info about it.")
    intro.draw(win)

    # Get points from mouse clicks
    c0 = win.getMouse()
    c0.draw(win)
    c1 = win.getMouse()
    c1.draw(win)

    # Create rectangle
    r = Rectangle(c0, c1)
    r.draw(win)

    # Getting side lengths
    dx = abs(c0.getX() - c1.getX())
    print("This rectangle's length is", dx)
    dy = abs(c0.getY() - c1.getY())
    print("This rectangle's height is", dy)

    # Getting area
    a = dx * dy
    print("This rectangle's area is", a)

    # Getting perimeter
    p = 2 *(dx + dy)
    print("This rectangle's perimeter is", p)

    win.getMouse()
    win.close()

main()
