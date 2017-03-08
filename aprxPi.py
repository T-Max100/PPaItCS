import math

def main():

    print()

    print("This should approximate the constant pi.")

    print()

    n = int(input("Please enter some integer value: "))

    pi = 0

    for d in range(n):
        pi = pi + ((4 / (2 * d + 1)) * (-1) ** d)

    print()

    print("The value of pi after running the formula", n, "times is", pi)

    e = abs(math.pi - pi)

    print("This differs from the actual value for pi by", e)
    print("Which by percentage is", 100 * (e / math.pi), "%")

    print()

main()
