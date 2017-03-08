from random import randint

# This is supposed to approximate the probability of five of a kind
# with five 6 sided dice

def main():
    n = 0 # Initializing a counter variable at 0
    k = int(input("How many die rolls? ")) # Getting user input
    for i in range(k): # A loop of length k
        FiveDieSet = set() # Create an empty set that represents the 5 die
        for j in range(5): # A loop of length 5
            d = randint(1,6) # d is one dice throw
            FiveDieSet.add(d) # Adding d to the set
        if len(FiveDieSet) == 1: # If the set has len of 1, die were same
            n += 1 # Increment if set has len 1.
    print(n)
    print(k)
    print(n/k)

if __name__ == '__main__': main()
