from graphics import *
from button import Button
from random import randint


def main():
    win = GraphWin("Three Button Monte", 600, 600)
    win.setCoords(0.0, 0.0, 6.0, 6.0)
    end = False
    points, count = 0, 0
    while end == False:
        greet(win)
        one, two, three = threeButtons(win)
        choice = pickDoor(win, one, two, three)
        points += conclusion(win, choice)
        count += 1
        score(win, points, count)
        end = quit_button(win)


def greet(win):
    message = Text(Point(3, 5.7), "Guess the correct door to win!")
    message.draw(win)
    win.getMouse()
    message.undraw()


def quit_button(win):
    QButton = Button(win, Point(0.5, 1.0), 0.5, 0.75, "Quit")
    QButton.activate()
    P = win.getMouse()
    if QButton.clicked(P):
        return True
    else:
        return False


def threeButtons(win):
    door_one = Button(win, Point(1.0, 3.0), 1, 3.0, "Door 1")
    door_one.activate()
    door_two = Button(win, Point(3.0, 3.0), 1, 3.0, "Door 2")
    door_two.activate()
    door_three = Button(win, Point(5.0, 3.0), 1, 3.0, "Door 3")
    door_three.activate()
    return door_one, door_two, door_three


def pickDoor(win, one, two, three):
    P = win.getMouse()
    if one.clicked(P):
        choice = [1, one.getLabel()]
        two.deactivate()
        three.deactivate()
    elif two.clicked(P):
        choice = [2, two.getLabel()]
        one.deactivate()
        three.deactivate()
    elif three.clicked(P):
        choice = [3, three.getLabel()]
        one.deactivate()
        two.deactivate()
    return choice


def conclusion(win, choice):
    points = 0
    door = randint(1, 3)
    win_message = "You Win!"
    lose_message = "You Lose! It was actually Door {}"
    if choice[0] == door:
        message = Text(Point(3, 5.7), win_message)
        points += 1
    elif choice[0] != door:
        message = Text(Point(3, 5.7), lose_message.format(door))
    message.draw(win)
    win.getMouse()
    message.undraw()
    return points


def score(win, points, count):
    message = Text(Point(5.5, 1.0), "Wins: {} Losses: {}".format(points, count - points))
    message.draw(win)
    win.getMouse()
    message.undraw()


if __name__ == "__main__":
    main()
