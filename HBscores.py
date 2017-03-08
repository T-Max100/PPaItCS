from graphics import *

def main():

    infileScores = input("What's the file name?: ")
    infile = open(infileScores, "r")

    # Create the window

    win = GraphWin("Scores", 720, 720)
    win.setCoords(0, 0, 10, 10)

    # Get number of columns

    nc = infile.readline()
    tnc = nc

    lc = -1

    # Draw names

    for line in infile:
        lc = lc + 2
        print("lc at this point is {}".format(lc))
        Text(Point(0.5, (10 - lc)), str(line[:-4])).draw(win)
        print("10 - lc at this point is {}".format(10 - lc))
        print("The name is {}".format(line[:-4]))
        bar = Rectangle(Point(1, (10.25 - lc)), Point((int(line[-3:]) / 10), (9.75 - lc)))
        print("The number is {}".format(line[-3:]))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    infile.close()
    win.getMouse()
    win.close()


main()
