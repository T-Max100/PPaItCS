import math

def main():

    print()

    print("The program implements Newton's method for computing square roots.")

    print()

    x = float(input("What number do you want the square root of?: "))

    n = int(input("How many times should the operation be run?: "))

    guess = float(input("What do you guess the square root is?: "))

    for i in range(n):
        guess = (guess + (x / guess)) / 2
        print(guess)

    print()

    print("After running the operation", n, "times, the guess is now", guess)

    print()

    print("This differs from the answer by", abs(math.sqrt(x) - guess))

    print()

main()
