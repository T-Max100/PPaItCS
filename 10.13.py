# face.py
from graphics import *
from button import Button

class Face:

        def __init__(self, window, center, size):
            eyeSize = 0.15 * size
            eyeOff = size / 3.0
            mouthSize = 0.8 * size
            mouthOff = size / 2.0
            self.head = Circle(center, size)
            self.head.draw(window)
            self.leftEye = Circle(center, eyeSize)
            self.leftEye.move(-eyeOff, -eyeOff)
            self.rightEye = Circle(center, eyeSize)
            self.rightEye.move(eyeOff, -eyeOff)
            self.leftEye.draw(window)
            self.rightEye.draw(window)
            p1 = center.clone()
            p1.move(-mouthSize / 2, mouthOff)
            p2 = center.clone()
            p2.move(mouthSize / 2, mouthOff)
            self.mouth = Line(p1, p2)
            self.mouth.draw(window)
            self.center = center
            self.size = size

        def smile(self, win):
            self.mouth.undraw()
            self.mouthOval = Oval(Point(80, 135), Point(120, 115))

            self.mouthOval.setFill("white")
            self.mouthOval.draw(win)

            self.mouthRectangle = Rectangle(Point(80, 125), Point(120, 115))
            self.mouthRectangle.setFill("white")
            self.mouthRectangle.setOutline("white")
            self.mouthRectangle.draw(win)

        def wink(self, win):
            self.mouth.undraw()
            self.rightEyeRectangle = Rectangle(Point((350 / 3) - 7.5,
                                                     (250 / 3)),
                                               Point((350 / 3) + 7.5,
                                                     (250 / 3) - 7.5))
            self.rightEyeRectangle.setFill("white")
            self.rightEyeRectangle.setOutline("white")
            self.rightEyeRectangle.draw(win)

        def frown(self, win):
            self.mouth.undraw()
            #self.mouthOval.undraw()
            #print(win.items)
            #print(self.mouthRectangle.draw(win))
            self.rightEyeRectangle.undraw()
            self.mouthRectangle.move(0, 10)


def main():
    win = GraphWin("Face")
    F = Face(win, Point(100, 100), 50)
    smileButton = Button(win, Point(25, 175), 35, 25, "Smile")
    smileButton.activate()
    winkButton = Button(win, Point(100, 175), 35, 25, "Wink")
    winkButton.activate()
    frownButton = Button(win, Point(175, 175), 35, 25, "Frown")
    frownButton.activate()
    win.getMouse()
    F.smile(win)
    win.getMouse()
    F.wink(win)
    win.getMouse()
    F.frown(win)
    win.getMouse()
    F
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
