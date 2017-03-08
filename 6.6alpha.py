# triangle.pyw
from graphics import *

def createLabeledWindow():
    window = GraphWin("Draw a Triangle", 300, 300)
    window.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(window)
    drawPoints(window)
    return window

def drawPoints(window):
    p1 = window.getMouse()
    p1.draw(window)
    p2 = window.getMouse()
    p2.draw(window)
    p3 = window.getMouse()
    p3.draw(window)
    drawTriangle(window, p1, p2, p3)
    getSides(window, p1, p2, p3)

def drawTriangle(window, t1, t2, t3):
    t = Polygon(t1, t2, t3)
    t.setFill("peachpuff")
    t.setOutline("cyan")
    t.draw(window)

def getSides(window, v0, v1, v2):
    # Getting side lengths
    s0x = abs(v1.getX() - v2.getX())
    s0y = abs(v1.getY() - v2.getY())
    s0 = (s0x ** 2 + s0y ** 2) ** 0.5
    print("This length of side 0 is", s0)
    s1x = abs(v0.getX() - v2.getX())
    s1y = abs(v0.getY() - v2.getY())
    s1 = (s1x ** 2 + s1y ** 2) ** 0.5
    s2x = abs(v0.getX() - v1.getX())
    s2y = abs(v0.getY() - v1.getY())
    s2 = (s2x ** 2 + s2y ** 2) ** 0.5
    heron(window, s0, s1, s2)

def heron(window, a, b, c):
    S = (a + b + c) / 2
    A = (S * (S -a) * (S -b) * (S -c)) ** 0.5
    message0 = Text(Point(5, 9.5), "The triangle's area is {}".format(A))
    message0.draw(window)
    # Wait for another click to exit
    message1 = Text(Point(5, 9.0), "Click anywhere to quit.")
    message1.draw(window)
    #message.setText("Click anywhere to quit.")
    window.getMouse()
    #print("The triangle's area is {}".format(A))

def main():
    print("This app uses Heron's formula to give the area of a triangle")
    print()
    win = createLabeledWindow()
    #drawPoints(win)
    #a, b, c = eval(input("Enter the triangle's three sides: "))
    #A = heron(a, b, c)
    #print()
    #print("The triangle's area is: ")
    print()
main()
