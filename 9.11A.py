from random import randint

# This is supposed to approximate the probability of five of a kind
# with five 6 sided dice

def main():
    n = 0 # Initializing a counter variable at 0
    m = int(input("How many die rolls? ")) # Getting user input
    for i in range(m): # A loop of length m
        FiveDieSet = {randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)} # Create a set with 5 random ints 1 - 6
        if len(FiveDieSet) == 1: # If the set has len of 1, die were same
        	n += 1 # Increment if set has len 1.
    print(n)
    print(m)
    print(n/m)

if __name__ == '__main__': main()


# Consider implementing Ivo's suggestion from here: http://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
