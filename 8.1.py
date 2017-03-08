# yet another fibonacci exercise. The one he did in the slides was elegant and awesome. Maybe I'll just use that one.

def fibo(n):
    b, a = 1, 0
    num = 0
    while num < n-1:
        b, a = a+b, b
        num += 1
    return b

def main():
    n = int(input("\nWhich Fibonacci number would you like to see?: "))
    print()
    print("Fibonacci number {} is {}\n".format(n, fibo(n)))
main()
