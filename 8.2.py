def windchill(T, V):
    w = (35.74) + (0.6215*T) - (35.75*(V**0.16)) + (0.4275*T*(V**0.16))
    return w

def main():
    print("\nWindchill index given wind speeds and temperatures")
    print("mph\°F|", end=' ')
    for T in range(-20, 61, 10):
        print("{:3d}".format(T), end='    ')
    print()
    print("-"*67)
    for V in range(0, 51, 5):
        print("{:3d}".format(V), end='    ')
        for T in range(-20, 61, 10):
            print(" {:3.0f}".format(windchill(T, V)), end='   ')
        print()
    print()
main()
