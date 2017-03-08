def GCD(m, n):
    while m != 0:
        n, m = m, n % m
    return n

def main():
    print("\nThis app calculates the greatest common denominator of two integers.")
    m = int(input("\nEnter integer one: "))
    n = int(input("\nEnter integer two: "))
    gcd = GCD(m, n)
    print("\nThe greatest common denominator of {} and {} is {}.\n".format(m, n, gcd))
main()
