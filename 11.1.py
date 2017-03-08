# stats.py
from math import sqrt

def getNumbers():
    nums = []     # start with an empty list

    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = eval(xStr)
        nums.append(x)   # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean(nums):
    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum / len(nums)

def stdDev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums)-1))

def meanStdDev(nums):
    mean = sum(nums) / len(nums)
    DevSq = [(num - mean) ** 2 for num in nums]
    return mean, (sum(DevSq) / (len(nums) - 1)) ** 0.5

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        median = (nums[midPos] + nums[midPos-1]) / 2.0
    else:
        median = nums[midPos]
    return median

def main():
    print("This program computes mean, median and standard deviation.")

    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)
    avg, StdDev = meanStdDev(data)

    print("\nThe mean is", xbar)
    print("The standard deviation is", std)
    print("The median is", med)
    print(f"The results of the new function gives a mean of {avg} and a standard deviation of {StdDev}.")

if __name__ == '__main__': main()
