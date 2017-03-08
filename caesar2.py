# I'm not sure that there's anyway to do this programming exercise well with what's been taight so far. Control statements would definitely solve some fundamental problems.

def main():

    mess = input("Enter a message: ")

    print("Your message is initially {0}".format(mess))

    key = int(input("Enter an integer as a key: "))

    print("Your key is {0}".format(key))

    abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz  ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

    msg = ""

    for ch in mess:
        print(msg)
        print(ch)
        msg = msg + (abc[abc.find(ch) + key])
        print("abc.find(ch) is {0}".format(abc.find(ch)))
        print("That, plus the key, equals {0}".format(abc.find(ch) + key))
        print("The character at that position in abc is {0}".format(abc[abc.find(ch) + key]))

    print(msg)

main()
