from graphics import *

def gui():

    #set up graphwin
    win = GraphWin('Regression Line',400,300)
    win.setCoords(0,0,40,30)
    win.setBackground('white')

    #CENTER origin of X,Y (0,0) is
    # X = -2
    # Y = -6.5
    #
    #Max value click never over this point
    # Xmax = 0 to 36 point
    # Ymax = 0 to 21.5 point
    #

    # color palette
    darkblue = color_rgb(11,119,229)
    lightblue = color_rgb(64,160,255)
    lightgrey = color_rgb(215,215,215)

    # draw blue box
    boxBluetop = Rectangle(Point(0,4),Point(40,4.5))
    boxBluetop.setFill(darkblue)
    boxBluetop.setWidth(0)
    boxBluetop.draw(win)

    boxBluebottom = Rectangle(Point(0,0),Point(40,4))
    boxBluebottom.setFill(lightblue)
    boxBluebottom.setWidth(0)
    boxBluebottom.draw(win)

    # draw description
    boxText = Text(Point(16.5,2.75),'Regression Line')
    boxText.setFace('times roman')
    boxText.setSize(12)
    boxText.setTextColor('white')
    boxText.draw(win)

    boxText2 = Text(Point(23.20,1),'Click to deploy data point and hit DONE when finish.')
    boxText2.setFace('times roman')
    boxText2.setSize(7)
    boxText2.setTextColor('white')
    boxText2.draw(win)

    # draw button
    buttonBorder = Rectangle(Point(0.5,0.4),Point(9.5,3.7))
    buttonBorder.setFill('black')
    buttonBorder.draw(win)

    button = Rectangle(Point(0.75,0.65),Point(9.25,3.5))
    button.setFill(lightgrey)
    button.draw(win)

    buttonText = Text(Point(5,2),'Done')
    buttonText.setFace('times roman')
    buttonText.setSize(12)
    buttonText.setTextColor('black')
    buttonText.draw(win)


    # draw x,y arm with indicator bar 1,5point
    Line(Point(2,6.5),Point(2,28)).draw(win)
    Line(Point(2,6.5),Point(38,6.5)).draw(win)

    # X bar
    for i in range(36):         #1point
        Line(Point(i+3,6.25),Point(i+3,6.75)).draw(win)
    for i in range(0,36,5):     #5point
        Line(Point(i+8,6.05),Point(i+8,6.95)).draw(win)

    # Y bar
    for i in range(21):         #1point
        Line(Point(1.75,i+7.5),Point(2.25,i+7.5)).draw(win)
    for i in range(0,21,5):     #5point
        Line(Point(1.55,i+11.5),Point(2.45,i+11.5)).draw(win)

    # setup warning text
    warn = Text(Point(20,18),'click inside field to input data.')
    warn.setSize(10)
    warn.setTextColor('red')

    # return what must be use in main() back
    return win,warn,buttonText

def dataProcess(pX,pY,num,xTotal,yTotal,xySigma,x2):

    # correct data with -2, -6.5 because graphic span
    pX = pX-2
    pY = pY-6.5

    num = num+1

    xTotal = xTotal+pX
    yTotal = yTotal+pY

    xySigma = xySigma + (pX*pY)

    x2 = x2+pX**2

    return num,xTotal,yTotal,xySigma,x2

def regressLine(num,xTotal,yTotal,xySigma,x2,win):

    xMean = xTotal/num
    yMean = yTotal/num

    m = (xySigma - (num*xMean*yMean)) / (x2 - (num*(xMean**2)))

    # find Y position according to X = 0,36
    # IF win.setCoords change, this must be modified too!!
    Ymin = yMean + m*(0-xMean)
    Ymax = yMean + m*(36-xMean)

    Rline = Line(Point(2,Ymin+6.5),Point(38,Ymax+6.5))
    Rline.draw(win)


def main():

    win,warn,buttonText = gui()

    num,xTotal,yTotal,xySigma,x2 = 0,0,0,0,0

    while True:
        p = win.getMouse()

        pX = p.getX()
        pY = p.getY()

        # if click inside field then compute data
        if 38 >= pX >= 2 and 28 >= pY >= 6.5:

            # remove warning if user click correctly
            warn.undraw()
            p.draw(win)

            num,xTotal,yTotal,xySigma,x2 = dataProcess(pX,pY,num,xTotal,yTotal,xySigma,x2)


        # if button clicked and have data point > 2 then draw line
        elif num >= 2 and 9.5 >= pX >= 0.5 and 3.7 >= pY >= 0.4:

            # remove warning if user click correctly
            warn.undraw()

            regressLine(num,xTotal,yTotal,xySigma,x2,win)

            break

        # user click something else
        else:
            # for second click it gets error if not undraw first
            warn.undraw()
            warn.draw(win)

    # click to close
    buttonText.setText('Close')
    win.getMouse()

if __name__ == '__main__': main()
