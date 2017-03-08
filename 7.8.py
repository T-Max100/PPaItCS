def eligibility(age, years):
    if age >= 30 and years >= 9:
        print("You're eligible for the senate and the house.")
    elif age >= 25 and years >= 7:
        print("You're only eligible for the house")
    else:
        print("You're not eligible to be a federal rep.")

def main():
    print()
    print("This app will tell you your eligibility for becoming a federal represntative.\n")
    try:
        A = int(input("How old are you?: "))
        print()
        Y = int(input("How many years have you been a ctiizen?: "))
        print()
        eligibility(A, Y)
    except ValueError:
        print("\nThe numbers you entered weren't quite right…")
    except NameError:
        print("\nOnly numbers please.")
    except TypeError:
        print("\nThe numbers you entered weren't quite right…")
    except SyntaxError:
        print("\nType it correctly next time buddy.")
    except:
        print("\nGeneral error. Terribly sorry.")
    print()
main()
