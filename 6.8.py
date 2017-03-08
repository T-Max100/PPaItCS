def nextGuess(guess, x):
    n = int(input("How many times should the operation be run?: "))
    for i in range(n):
        guess = (guess + (x / guess)) / 2
        print(guess)
    print("After running the operation {} times, the guess is now {}".format(n, guess))
    print()
    print("This differs from the answer by {:0.6f}".format(abs(x ** 0.5 - guess)))

def main():
    print()
    print("The program implements Newton's method for computing square roots.")
    print()
    x = float(input("What number do you want the square root of?: "))
    guess = float(input("What do you guess the square root is?: "))
    print()
    nextGuess(guess, x)
    print()
main()
