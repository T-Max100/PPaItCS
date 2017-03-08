def main():

    print()

    print("This program computes the nth Fibonacci number where n is a")
    print("value input by the user. For example, if n = 6, then the result")
    print("is 8.")

    print()

    n = int(input("Type a whole number: "))

    print()

    fib = 0

    a = 0
    b = 1

    for e in range(n - 1):
        #fib = fib + e
        #print(fib)
        c = a + b
        #print(c)
        a, b = b, c

    print()

    print("The number is", c)

    print()

main()
