def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums

def main():
    l = [8, 16, 19, 14, 18]
    print(l)
    print("The squares of the above are {}".format(squareEach(l)))
main()
