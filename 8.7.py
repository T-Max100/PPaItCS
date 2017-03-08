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

def primelist(x):
    l = []
    n = x - 1
    while n >= 2:
        if primes(n) == True:
            l.append(n)
            n -= 1
        else:
            n -= 1
    print("l = ", l)
    return l

def gold(x, li):
    for num in li:
        print("num = ", num)
        r = x - num
        print("r =", r)
        if r in li:
            return r, num
        else:
            print("\nConjecture fails\n")

def main():
    print("\nThis app checks Goldbach's conjecture.")
    x = int(input("\nEnter an even number: "))
    if x % 2 == 0:
        li = primelist(x)
        print("li =", li)
        r, num = gold(x, li)
        print("\n{} can be made by combining prime numbers {} and {}.\n".format(x, r, num))
    else:
        print("\nThat's not an even number.\n")
main()
