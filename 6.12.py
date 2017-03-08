def sumList(nums):
    Sum = 0
    for i in range(len(nums)):
        Sum = Sum + nums[i]
    return Sum

def main():
    l = [8, 16, 19, 14, 18]
    print(l)
    print("The sum of the above is {}".format(sumList(l)))
main()
