def grade(score):
    grades = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]
    print("\nThat score corresponds to a grade of {}.\n".format(grades[score // 10]))

def main():
    score = int(input("\nOn a 0 - 100 scale, what's the score?: "))
    grade(score)
main()
