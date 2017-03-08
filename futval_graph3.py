# futval_graph3.py
# might be improved by allowing the program to produce another graphics window which has its dimensions dynamically determined by paramters decided by the user.
# Finished this. It was difficult but worth it. Lots of trial and error debugging/fixing. Perry suggests following the scientific method for debugging. I like the sound of it.

from graphics import *

def main():

    # Create the window

    win = GraphWin("Investment Growth Chart", 720, 720)
    win.setCoords(0, 0, 30, 32000)

    # Prompt user with UI

    O = Text(Point(13.5, 31000), "This program calculates the future value of an investment over a specified number of years. Click mouse to move forwards.")
    O.draw(win)
    win.getMouse()

    P = Text(Point(3.5, 29000), "Enter the initial principal:")
    P.draw(win)
    UEP = Entry(Point(8, 29000), 10)
    UEP.setText("0")
    UEP.draw(win)
    win.getMouse()

    Y = Text(Point(3.5, 28000), "Enter the number of years:")
    Y.draw(win)
    UEY = Entry(Point(8, 28000), 10)
    UEY.setText("0")
    UEY.draw(win)
    win.getMouse()

    F = Text(Point(3.5, 27000), "Enter the fixed contribution:")
    F.draw(win)
    UEF = Entry(Point(8, 27000), 10)
    UEF.setText("0")
    UEF.draw(win)
    win.getMouse()

    I = Text(Point(3.5, 26000), "Enter  the  interest  rate:")
    I.draw(win)
    UEI = Entry(Point(8, 26000), 10)
    UEI.setText("0.00")
    UEI.draw(win)
    win.getMouse()

    C = Text(Point(3.5, 25000), "Enter # of compoundings:")
    C.draw(win)
    UEC = Entry(Point(8, 25000), 10)
    UEC.setText("0.00")
    UEC.draw(win)
    win.getMouse()

    s = Text(Point(3.5, 24000), "Click window to continue")
    s.draw(win)

    # Get user confirmation with a mouse click, then undraw the stuff

    win.getMouse()
    s.undraw()
    UEC.undraw()
    C.undraw()
    UEI.undraw()
    I.undraw()
    UEF.undraw()
    F.undraw()
    UEY.undraw()
    Y.undraw()
    UEP.undraw()
    P.undraw()
    O.undraw()

    # Process input with UI for user

    Text(Point(1, 0), '  0.0K').draw(win)
    Text(Point(1, 2500),  ' 50.0K').draw(win)
    Text(Point(1, 5000),  '100.0K').draw(win)
    Text(Point(1, 7500),  '150.0k').draw(win)
    Text(Point(1, 10000), '200.0K').draw(win)
    Text(Point(1, 12500), '250.0K').draw(win)
    Text(Point(1, 15000), '300.0K').draw(win)
    Text(Point(1, 17500), '350.0K').draw(win)
    Text(Point(1, 20000), '400.0K').draw(win)
    Text(Point(1, 22500), '450.0K').draw(win)
    Text(Point(1, 25000), '500.0K').draw(win)
    Text(Point(1, 27500), '550.0K').draw(win)
    Text(Point(1, 30000), '600.0K').draw(win)

    # Draw bar for initial principal
    principal = float(UEP.getText())
    print(principal)
    years = int(UEY.getText())
    print(years)
    FC = float(UEF.getText())
    print(FC)
    rate = float(UEI.getText())
    print(rate)
    periods = float(UEC.getText())
    print(periods)
    bar = Rectangle(Point(2, 0), Point(3, principal / 20))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw a bar for each subsequent year
    for i in range(years):
        P = principal
        r = rate
        n = periods
        t = i + 1
        A = (FC * (((1 + (r / n)) ** (n * t) - 1) / (r / n)) * (1 + (r / n))) + (P * (1 + r / n) ** (n * t))
        print(round(A,2))
        bar = Rectangle(Point(i+3, 0), Point(i+4, A / 20))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        win.getMouse()

    rounded_A = round(A,2)
    Text(Point(13.5, 31000), "The final value is").draw(win)
    output = Text(Point(16.5, 31000),"")
    output.draw(win)
    win.getMouse()
    output.setText(rounded_A)
    win.getMouse()
    input("Press <Enter> to quit.")

    win.close()


main()
