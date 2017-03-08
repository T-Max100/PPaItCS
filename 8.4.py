def syr(x):
    s = []
    s.append(x)
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            #print(x)
            s.append(x)
            #print(s)
        else:
            x = 3 * x + 1
            #print(x)
            s.append(x)
            #print(s)
    return s

def main():
    print("\nThis prints the Syracuse sequence for any integer.")
    x = int(input("\nEnter the integer of your choice: "))
    Syr = syr(x)
    #print(Syr)
    print("The Syracuse sequence for {} is {}. That's a length of {}\n".format(x, Syr, len(Syr)))
main()
