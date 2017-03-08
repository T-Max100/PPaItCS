def main():

    mess = input("Enter a message and a number separated by a comma: ")

    msg = mess.split(",")

    w = ""

    for ch in msg[0]:
        w = w + chr(ord(ch) + int(msg[1]))

    print(w)

main()
