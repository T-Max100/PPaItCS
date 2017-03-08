def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return strList

def sumList(nums):
    Sum = 0
    for i in range(len(nums)):
        Sum = Sum + nums[i]
    return Sum

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums

def main():
    infileNums = input("What file are the numbers in?: ")

    infile = open(infileNums, "r")

    for line in infile:
        print(line)
        Sline = line.split(",")
        print("The above as numbers: {}".format(toNumbers(Sline)))
        print("The sum of the above numbers: {}".format(sumList(Sline)))
        print("The squares of the numbers are {}".format(squareEach(Sline)))

    infile.close()
main()
