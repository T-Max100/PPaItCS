def sumN(n):
    Sum = 0
    for i in range(1, n + 1):
        Sum = Sum + i
    return Sum

def sumNCubes(n):
    Sum = 0
    for i in range(1, n + 1):
        Sum = Sum + i ** 3
    return Sum

def main():
    n = int(input("Enter an integer n: "))
    print("The the sum of first n natural numbers is {}".format(sumN(n)))
    print("The the sum of the cubes of the first n natural numbers is {}".format(sumNCubes(n)))
main()
