from graphics import *
from button import Button

win = GraphWin("Test Buttons", 480, 480)
win.setBackground("White")
win.setCoords(0, 0, 480, 480)
win.getMouse()

testButton = Button(win, Point(240, 240), 200, 150, "test")
win.getMouse()
testButton.activate()

win.getMouse()

testButton.changeText(win, Point(240, 240), "Finished")

win.getMouse()
win.close()
