def prime(n):
    x = 0
    if n % 2 == 0:
        return 2
    elif n in [3, 5, 7]:
        print("\n{} is prime".format(n))
        return n
    else:
        d = 3
        while d <= n ** 0.5:
            if n % d == 0:
                print("\n{} is not prime".format(n))
                return d
            elif n % d != 0:
                if n ** 0.5 - d < 1:
                    print("\n{} is prime".format(n))
                    return n
                else:
                    d += 1

def main():
    print("\nThis app determines if a number is prime or not.")
    n = int(input("\nEnter a number: "))
    print("\n{} is divisible by {}\n".format(n, prime(n)))
main()
