# File: chaos2: Electric Boogaloo
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic fuction")
    x = float(input("Enter a number between 0 and 1: "))
    y = float(input("Enter another number between 0 and 1: "))
    n = int(input("How many numbers should I print? "))
    print()
    print("index", str(x).center(9), str(y).rjust(10))
    print("-" * 28)
    for i in range(n):
        x = 3.9 * x * (1 -x)
        y = 3.9 * y * (1 -y)
        print('{} {:11.6f} {:12.6f}'.format(str(i + 1).rjust(3), x, y))

main()
