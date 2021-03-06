from graphics import *
from button import Button
from random import randint

def main():
    win = GraphWin("Three Button Monte", 600, 600)
    win.setCoords(0.0, 0.0, 6.0, 6.0)
    greet(win)
    one, two, three = threeButtons(win)
    choice = pickDoor(win, one, two, three)
    win_lose = conclusion(win, choice)

def greet(win):
    message = Text(Point(3, 5.7), "Guess the correct door to win!")
    message.draw(win)
    win.getMouse()
    message.undraw()
    
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
    door = randint(1,3)
    win_message = "You Win!"
    lose_message = "You Lose! It was actually Door {}"
    if choice[0] == door:
        message = Text(Point(3, 5.7), win_message)
    elif choice[0] != door:
        message = Text(Point(3, 5.7), lose_message.format(door))
    message.draw(win)
    win.getMouse()
    message.undraw()
    win.close()
    
if __name__ == "__main__":
    main()
