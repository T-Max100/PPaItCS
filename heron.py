print()

def main():
    print("This app uses Heron's formula to give the area of a triangle")
    print()
    a, b, c = eval(input("Enter the triangle's three sides: "))
    S = (a + b + c) / 2
    A = (S * (S -a) * (S -b) * (S -c)) ** 0.5
    print()
    print("The triangle's area is: ", A)
    print()
main()
