# month2.py
# A program to print the month abbreviation, given its number.

def main():

    # months is a list used as a lookup table
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    n = eval(input("Enter a month number (1-12): "))

    print("The month abbreviation is", months[n-1] + ".")

main()
