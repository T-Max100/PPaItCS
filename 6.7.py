def fibo(n):
    fib = 0
    a = 0
    b = 1
    for e in range(n - 1):
        c = a + b
        a, b = b, c
    return c

def main():
    print()
    print("This app computes the nth Fibonacci number.\n")
    n = int(input("Enter an integer n: "))
    fibon = fibo(n)
    print()
    print("That Fibonacci number is {}.".format(fibon))
main()
