def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return strList

def main():
    l = ["8", "16", "19", "14", "18"]
    print(l)
    print("The above as integers is {}".format(toNumbers(l)))
main()
