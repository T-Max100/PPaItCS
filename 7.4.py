def standing(credits):
    if credits >= 26:
        stand = "Senior"
    elif credits >= 16:
        stand = "Junior"
    elif credits >= 7:
        stand = "Sophomore"
    else:
        stand = "Freshman"
    return stand

def main():
    print()
    C = int(input("How many credits have you got?: "))
    print()
    print("That makes a {} at this institution.\n".format(standing(C)))
main()
