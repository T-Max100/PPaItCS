from graphics import *
from time import sleep

def main():
    win = GraphWin('Ball Animation',500,350)
    win.setCoords(0,0,20,14)

#display grid
#    for i in range(1,20):
#        Line(Point(i,0),Point(i,14)).draw(win)
#        Line(Point(0,i),Point(20,i)).draw(win)

    #where the ball start appear...
    BallCenter = Point(10,7)

    #how big the ball is...
    radius = 2

    #speed direction of ball...
    dx,dy = 1,1

    #speed of ball animation use with sleep()
    speed = 0.005

    #Use border Min/Max to check if ball hit border or not
    XborderMax = 20-radius
    XborderMin = 0+radius
    YborderMax = 14-radius
    YborderMin = 0+radius

    #draw ball on center
    ball = Circle(BallCenter,radius)
    ball.setFill('red')
    ball.setOutline('red')
    ball.draw(win)

    #Show "Click to Start!"
    start = Text(BallCenter,'Click to Start!')
    start.setSize(36)
    start.draw(win)

    win.getMouse()
    start.undraw()

    #start the loop animation
    for i in range(1000):

        #get center of ball
        now = ball.getCenter()

        #now compare X,Y to the Max/Min border
        #if it reach any border change direction
        if now.getX() >= XborderMax:
            dx = -1
        if now.getX() <= XborderMin:
            dx = 1
        if now.getY() >= YborderMax:
            dy = -1
        if now.getY() <= YborderMin:
            dy = 1

        #move ball
        ball.move(dx,dy)

        #make animation slow to watch
        sleep(speed)

    #end loop then close windows
    win.close()

#if __name__ == '__main__': main()
main()
