# Program: triangle2.py
import math
from graphics import *

def heron(a, b, c):
    S = (a + b + c) / 2
    A = (S * (S -a) * (S -b) * (S -c)) ** 0.5
    return A

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist

def main():
    win = GraphWin("Draw a Triangle", 333, 333)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    win.getMouse()
    message.setText("The perimeter is: {0:0.2f}".format(perim))

    # Calculate the area of the triangle
    area = heron(distance(p1,p2), distance(p2,p3), distance(p3,p1))
    win.getMouse()
    message.setText("The area is: {0:0.2f}".format(area))

    # Wait for another click to exit
    win.getMouse()
    win.close()

main()
