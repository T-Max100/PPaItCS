def grades(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score < 60:
        grade = "F"
    return grade

def main():
    print()
    S = int(input("On a 0 to 100 scale, what's the score?: "))
    print()
    print("That's equivalent to a grade of {}\n".format(grades(S)))
main()
