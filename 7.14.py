# chose circle radius of 2 and a y-intercept of 4. That caused a TypeError regarding complex numbers that couldn't be converted to integers.

from graphics import *

def main():
    win = GraphWin("Circle Intersection", 1000, 1000)
    win.setBackground(color_rgb(128,128,128))
    win.setCoords(-10, -10, 10, 10)

    # Draw interface and intro program
    intro = Text(Point(0, 9.5), "This will make a circle in the center and a horizontal line touching at the y-intercept. Click window to move forwards.")
    intro.draw(win)

    # Take user input
    r = Text(Point(-1.5, 9.0), "Enter the radius of the circle:")
    r.draw(win)
    R = Entry(Point(1, 9.0), 10)
    R.setText("0")
    R.draw(win)
    win.getMouse()

    y = Text(Point(-1.5, 8.5), "Enter the y-intercept of the line:")
    y.draw(win)
    Y = Entry(Point(1, 8.5), 10)
    Y.setText("0")
    Y.draw(win)
    win.getMouse()

    # Draw circle and line based on user input
    P = Point(0, 0)

    rad = float(R.getText())
    yint = float(Y.getText())
    lp1 = Point(-10, yint)
    lp2 = Point(10, yint)

    C = Circle(P, rad)
    C.draw(win)

    L = Line(lp1, lp2)
    L.setFill("green")
    L.draw(win)

    # Calculate x values
    try:
        x1 = (rad ** 2 - yint ** 2) ** 0.5
        print(x1)
        x2 = -((rad ** 2 - yint ** 2) ** 0.5)
        print(x2)

        # Make the points of intersection red
        P1 = Point(x1,yint)
        P1.setFill("red")
        P1.draw(win)

        P2 = Point(x2,yint)
        P2.setFill("red")
        P2.draw(win)
    except TypeError as excObj:
        if str(excObj) == "can't convert complex to int":
            print("The line and the circle do not intersect.")

    win.getMouse()
    win.close()

main()
