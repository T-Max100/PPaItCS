def count(myList, x):
    total = 0
    for item in myList:
        if item == x:
            total += 1
    return total

def isin(myList, x):
    for item in myList:
        if item == x:
            return True
    return False

def index(myList, x):
    for index, item in enumerate(myList):
        if item == x:
            return index

def reverse(myList):
    return myList[::-1]

# def sort(myList):
#     loNum = 0
#     hiNum = 0
#     loABC = ''
#     hiABC = ''
#     iList = iter(myList)
#     Type = type(next(iList))
#     if all((type(x) is Type) for x in iList) and Type == str:

print(f"count([1, 2, 2, 3, 5], 2) == {count([1, 2, 2, 3, 5], 2)}, and [1, 2, 2, 3, 5].count(2) == {[1, 2, 2, 3, 5].count(2)}")
print(f"isin(['a', 'b', 'c', 'd'], 'c') == {isin(['a', 'b', 'c', 'd'], 'c')} and 'c' in ['a', 'b', 'c', 'd'] == {'c' in ['a', 'b', 'c', 'd']}")
print(f"index([0, 1, 2, 3, 4], 4) == {index([0, 1, 2, 3, 4], 4)} and [0, 1, 2, 3, 4].index(4) == {[0, 1, 2, 3, 4].index(4)}")
print(f"reverse([1, 2, 3, 4, 5]) == {reverse([1, 2, 3, 4, 5])} and [1, 2, 3, 4, 5].reverse() == {[1, 2, 3, 4, 5].reverse()}")
