from graphics import *

def createLabeledWindow():
    win = GraphWin("Archery", 500, 500)
    win.setBackground(color_rgb(128,128,128))
    win.setCoords(-2.5, -2.5, 2.5, 2.5)
    drawTarget(win)
    message = Text(Point(0, 2.375), "Click on five points")
    message.draw(win)
    win.getMouse()
    message.undraw()
    drawPoints(win)
    return win

def drawTarget(window):
    win = window
    p = Point(0, 0)
    c = ["white", "black", "blue", "red", "yellow"]

    for i in range(len(c)):
        O = Circle(p, 2.5 - i * 0.5)
        O.setFill(c[i])
        O.setOutline(c[i])
        O.draw(win)

def drawPoints(window):
    total = 0
    for i in range(5):
        p = window.getMouse()
        p.draw(window)
        if 0 <= (p.getX() ** 2 + p.getY() ** 2) ** 0.5 <= 0.5:
            total += 9
        elif 0.5 <= (p.getX() ** 2 + p.getY() ** 2) ** 0.5 <= 1.0:
            total += 7
        elif 1.0 <= (p.getX() ** 2 + p.getY() ** 2) ** 0.5 <= 1.5:
            total += 5
        elif 1.5 <= (p.getX() ** 2 + p.getY() ** 2) ** 0.5 <= 2.0:
            total += 3
        elif 2.0 <= (p.getX() ** 2 + p.getY() ** 2) ** 0.5 <= 2.5:
            total += 1
        else:
            total += 0
    print(total)

def main():
    print()
    print("This app draws a target and awards points for shots with the mouse.")

    win = createLabeledWindow()

    win.getMouse()
    win.close()
    print()
main()
