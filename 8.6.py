def primes(n):
    if n in [2, 3, 5, 7]:
        #print("\n{} is prime".format(n))
        return True
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d <= n ** 0.5:
            if n % d == 0:
                #print("\n{} is not prime".format(n))
                return False
            elif n % d != 0:
                if n ** 0.5 - d < 1:
                    #print("\n{} is prime".format(n))
                    return True
                else:
                    d += 1

def main():
    l = []
    print("\nThis app determines the prime numbers under a number.")
    x = int(input("\nEnter a number: "))
    n = x - 1
    while n >= 2:
        if primes(n) == True:
            l.append(n)
            n -= 1
        else:
            n -= 1
    print("\nThe prime numbers under {} are:\n{}".format(x, l))
    print("\nThat's {} numbers.\n".format(len(l)))
main()
