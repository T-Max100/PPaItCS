def main():
    score = int(input("\nOn a 0 - 5 scale, what's the score?: "))

    grades = ["F", "F", "D", "C", "B", "A"]

    print("\nThat score corresponds to a grade of {}.\n".format(grades[score]))
main()
