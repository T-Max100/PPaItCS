from graphics import *

def main():

    # Create the window

    win = GraphWin("Investment Growth Chart", 720, 720)
    win.setCoords(0, 0, 30, 32000)

    # Prompt user with UI

    Text(Point(3.5, 32000 - (4000 / 3)), "Enter the initial principal:").draw(win)
    UEP = Entry(Point(8, 32000 - (4000 / 3)), 10)
    UEP.setText("0.00")
    UEP.draw(win)
    #win.getMouse()
    Text(Point(3.5, 29000), "Enter  the  interest  rate:").draw(win)
    UEI = Entry(Point(8, 29000), 10)
    UEI.setText("0.00")
    UEI.draw(win)
    #win.getMouse()
    Text(Point(3.5, 29000 - (5000 / 3)), "Click window to continue").draw(win)


    # Get user confirmation with a mouse click

    win.getMouse()

    # Process input with UI for user

    Text(Point(1, 0), ' 0.0K').draw(win)
    Text(Point(1, 2500), ' 2.5K').draw(win)
    Text(Point(1, 5000), ' 5.0K').draw(win)
    Text(Point(1, 7500), ' 7.5k').draw(win)
    Text(Point(1, 10000), '10.0K').draw(win)

    # Draw bar for initial principal
    principal = float(UEP.getText())
    apr = float(UEI.getText())
    bar = Rectangle(Point(2, 0), Point(3, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year+2, 0), Point(year+3, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        win.getMouse()

    input("Press <Enter> to quit.")


    #win.getMouse()
    win.close()


main()
