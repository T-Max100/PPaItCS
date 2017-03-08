# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    print("This program is designed to convert Fahrenheit temperatures into Celsius temperatures.")

    F = eval(input("What is the Fahrenheit temperature? "))

    C = 5/9 * (F - 32)

    print("The temperature is", C, "degrees Celsius.")

main()
