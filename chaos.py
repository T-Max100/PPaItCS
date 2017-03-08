# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic fuction")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 -x)
        y = 3.9 * y * (1 -y)
        print('{0:2f} {1:3f}'.format(x, y))

main()
