import math
from random import random
from graphics import *
 
 
class Button:
 
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""
 
    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """
 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
 
    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
 
    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()
 
    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setFill('green')
        self.rect.setWidth(2)
        self.active = True
 
    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
         
 
def main():
    win,input,walker,bStart = drawGUI()
    n = getInput(win,input,bStart)
    x,y = randomWalk(n,win,walker)
    printSummary(win,n,x,y)
    exit(win,bStart)
     
 
 
 
def drawGUI():
     
    win = setupWindow()
    drawPark(win)
    walker = drawWalker(win)
    input = drawText(win)
    bStart = drawButton(win)   
 
    return win,input,walker,bStart
     
     
     
 
def setupWindow():
    win = GraphWin('Random Walk with graphic.',600,360)
    win.setBackground('White')
    win.setCoords(0,0,200,120)
     
    return win
 
 
 
 
def drawPark(win):
     
    park = Rectangle(Point(10,10),Point(110,110))
    park.setFill(color_rgb(140,234,153))
    park.setWidth(0)
    park.draw(win)
     
    for i in range(21):
        i = i*5
        Line(Point(i+10,10),Point(i+10,110)).draw(win)
        Line(Point(10,i+10),Point(110,i+10)).draw(win)
         
        Xaxis = Text(Point(i+10,7),-50+i)
        Xaxis.setSize(5)
        Xaxis.draw(win)
         
        Yaxis = Text(Point(7,i+10),-50+i)
        Yaxis.setSize(5)
        Yaxis.draw(win)
         
 
 
def drawWalker(win):
     
    walker = Circle(Point(60,60),3)
    walker.setFill('Red')
    walker.setWidth(0)
    walker.draw(win)
     
    return walker
     
     
 
def drawText(win):
 
    title = Text(Point(155,105),'RandomWalk GUI')
    title.setSize(18)
    title.setFace('times roman')
    title.draw(win)
     
    intro1 = Text(Point(155,90),'Please enter how many steps')
    intro2 = Text(Point(150,83),'to simulate random walk.')
     
    intro1.setSize(12)
    intro2.setSize(12)
    intro1.draw(win)
    intro2.draw(win)
     
    input = Entry(Point(137,72),10)
    input.setText('0')
    input.draw(win)
     
    return input
 
 
 
#draw Start button
def drawButton(win):
     
    #use class Button() instead of Graphic Rectangle()
    bStart = Button(win, Point(133,56), 24, 8, 'Start!')
    bStart.activate()
     
    return bStart 
 
 
def getInput(win,input,bStart):
     
    n = retry = 0   
 
    p = win.getMouse()
    n = input.getText()
    n = int(n)
     
    #loop if not click button and not provide correct value
    while not bStart.clicked(p) or n <= 0:
         
        #if user clicked but not give corract value ware him
        if bStart.clicked(p) == True:
            if retry == 0:
                retry = 1
                warn = wrongInput(win)
             
        p = win.getMouse()
        n = input.getText()
        n = int(n)
 
    if retry == 1 : warn.undraw()
     
    return n
 
 
 
def wrongInput(win):
    warn = Text(Point(155,30),'Wrong value.\n Please correct your input')
    warn.setFill('red')
    warn.draw(win)
     
    return warn
     
     
     
def randomWalk(n,win,walker):
     
    x = y = 60
     
    for i in range(n):
         
        xStep,yStep = walk()
        gMoveTo(walker,xStep,yStep)       
        tracing(win,x,y,xStep,yStep)
         
        x = x+xStep
        y = y+yStep
 
    return x-60,y-60
         
 
 
def walk():
    angle = randomAngle()
    xStep = math.cos(angle)
    yStep = math.sin(angle)
     
    return xStep,yStep
 
 
def randomAngle():
    return random()*2*math.pi
     
 
 
def gMoveTo(walker,xStep,yStep):
    walker.move(xStep,yStep)
     
 
 
def tracing(win,x,y,xStep,yStep):
     
    tracing = Line(Point(x,y),Point(x+xStep,y+yStep))
    tracing.setFill('red4')
    tracing.draw(win)
     
 
 
def printSummary(win,n,x,y):
     
    Text(Point(155,40),'After {} steps'.format(n)).draw(win)
    Text(Point(155,35),'the last position of walker is at').draw(win)
    Text(Point(155,25),'X = {}'.format(round(x,2))).draw(win)
    Text(Point(155,20),'Y = {}'.format(round(y,2))).draw(win)
 
 
 
def exit(win,bStart):
     
    #deactivate the button
    bStart.deactivate()
    bye = Text(Point(155,10),'click anywhere to close')
    bye.setFill('red')
    bye.setSize(15)
    bye.draw(win)
     
    win.getMouse()
    win.close()
 
if __name__ == '__main__': main()
