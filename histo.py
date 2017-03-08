from graphics import *

def main():

    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    infileScores = input("What's the file name?: ")
    infile = open(infileScores, "r")

    nums = infile.read()

    # Create the window

    win = GraphWin("Scores", 720, 720)
    win.setCoords(0, 0, 20, 20)

    ln = 0

    # Core logic

    for i in range(11):
        l[i] = nums.count(str(i))

    l[0] = l[0] - l[10]

    for i in range(len(l)):
        Text(Point(i + 5, 0), str(i)).draw(win)
        bar = Rectangle(Point(i + 4.5, l[i]), Point(i + 5.5, 1))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    """
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
        """


    infile.close()
    win.getMouse()
    win.close()


main()
