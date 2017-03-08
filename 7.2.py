def grades(score):
    if score == 5:
        grade = "A"
    elif score == 4:
        grade = "B"
    elif score == 3:
        grade = "C"
    elif score == 2:
        grade = "D"
    elif score <= 1:
        grade = "F"
    return grade

def main():
    print()
    S = int(input("On a 0 to 5 scale, what's the score?: "))
    print()
    print("That's equivalent to a grade of {}\n".format(grades(S)))
main()
