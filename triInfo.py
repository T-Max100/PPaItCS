from graphics import *

def main():

    # Create the window
    win = GraphWin("Line Segment Information", 1000, 1000)
    win.setCoords(0, 0, 1000, 1000)

    # Explain to user what the app does
    intro = Text(Point(250, 975), "This app will draw a triangle between three mouse clicks and give some info about it.")
    intro.draw(win)

    # Get points from mouse clicks
    v0 = win.getMouse()
    v0.draw(win)
    print("The coordinates of vertex 0 are", v0.getX(), v0.getY())
    v1 = win.getMouse()
    v1.draw(win)
    print("The coordinates of vertex 1 are", v1.getX(), v1.getY())
    v2 = win.getMouse()
    v2.draw(win)
    print("The coordinates of vertex 2 are", v2.getX(), v2.getY())

    # Create triangle
    t = Polygon(v0, v1, v2)
    t.draw(win)

    # Getting side lengths
    s0x = abs(v1.getX() - v2.getX())
    s0y = abs(v1.getY() - v2.getY())
    s0 = (s0x ** 2 + s0y ** 2) ** 0.5
    print("This length of side 0 is", s0)
    s1x = abs(v0.getX() - v2.getX())
    s1y = abs(v0.getY() - v2.getY())
    s1 = (s1x ** 2 + s1y ** 2) ** 0.5
    print("This length of side 1 is", s1)
    s2x = abs(v0.getX() - v1.getX())
    s2y = abs(v0.getY() - v1.getY())
    s2 = (s2x ** 2 + s2y ** 2) ** 0.5
    print("This length of side 2 is", s2)

    # Getting the perimeter
    p = s0 + s1 + s2
    print("The triangle's perimeter is", p)

    # Getting the area
    s = (s0 + s1 + s2) / 2
    a = (s * (s - s0) * (s - s1) * (s - s2)) ** 0.5
    print("The triangle's area is", a)

    win.getMouse()
    win.close()

main()
