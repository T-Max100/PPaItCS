# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    print("This program is designed to convert Celsius temperatures into Fahrenheit temperatures.")
    for i in range(11):
#        C = eval(input("What is the Celsius temperature? "))
        C = i * 10
        F = 9/5 * C + 32
#        print("The temperature is", F, "degrees Fahrenheit.")
        print(C, F)

main()
