def BMI(weight, height):
    bmi = (weight) / (height ** 2)
    if bmi > 25:
        print("Your BMI is {:.0f}. That's above the healthy range.".format(bmi))
    elif 19 <= bmi <= 25:
        print("Your BMI is {:.0f}. That's considered healthy!".format(bmi))
    elif bmi < 19:
        print("Your BMI is {:.0f}. That's below the healthy range.".format(bmi))

def main():
    print()
    print("This app calculates your body mass index (BMI) from your\nweight (in kg) and your height (in m).\n")
    W, H, = eval(input("Enter your weight in kg and height in m (W, H): "))
    print()
    BMI(W, H)
main()
