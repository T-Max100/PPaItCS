"""
Given a list of intervals, e.g [1,3) [4,5) [1,2) [2,3) give back a possibly smaller list of them merged

E.g. [1,3) [4,5)

Started at 10 AM
"""

# Ok, sorted() works on the list of tuples. The example one aranges to [(1, 2), (1, 3), (2, 3), (4, 5)]. We can note that there's a gap of more than one in the first element between 2 and 4. Note also the gap of more than one from the second element between the 3 and 5.

# Since tuples are immutable… quick stop to verify that statement… ok, since tuples are imumtable I'm not going to be changing the tuples in the list in place, instead I'm making a new list with new tuples.

# I think a for loop will do the trick here, then a list comprehension. Planning out the for loop:
"""
sList = sorted(lis)
newEnds, merged = [[], []], [[], []]
newEnds[0].append(sList[0][0])
newEnds[-1].append(sList[-1][-1])

for i in range(len(sList) - 1):
    if sList[i + 1][0] - sList[i][0] > 1:
        newEnds[0].append(sList[i + 1][0])
    if sList[i + 1][1] - sList[i][1] > 1:
        newEnds[1].insert(0, sList[i][1])

for sub in newEnds:
    merged[0].append(sub[0])
    merged[1].append(sub[1])

for i in range(len(merged)):
    merged[i] = tuple(merged[i])

print(merged)
"""

# Ended at 11:30, probably really got started around 10:15

# Crap, realized that I solved only for the specific case and not the general one. I'm not sure how long it would take to reflow this.

# started in earnest at 11:40

"""
This time I'm just going to append the numbers directly to a list, and then tuple consecutive pairs of numbers.

sList = sorted(lis) # i.e. [(1, 2), (1, 3), (2, 3), (4, 5)]
newEnds, merged = [], []
# newEnds.append(sList[0][0]) # might save this for the end
# newEnds.insert(-1, sList[-1][-1]) # might save this for the end

# assume that there's a (9, 10) that's just been added

for i in range(len(sList) - 1):
    if sList[i + 1][0] - sList[i][0] > 1:
        newEnds.append(sList[i + 1][0])
    if sList[i + 1][1] - sList[i][1] > 1:
        newEnds.insert(0, sList[i][1])

newEnds = [5, 3, 4, 9]
newEnds = [1, 5, 3, 4, 9, 10]
sorted
newEnds = [1, 3, 4, 5, 9, 10]
for i in range(0, len(newEnds) - 1, 2):
    merged.append(tuple([i:i + 2]))

Finished again about 12:15
"""

# assuming some list of tuples named lis
"""
lis = [(1, 5), (2, 4), (3, 6)]
sList = sorted(lis)
newEnds, merged = [], []
newEnds.extend((sList[0][0], sList[-1][-1]))

for i in range(len(sList) - 1):
    if sList[i + 1][0] - sList[i][0] > 1:
        newEnds.append(sList[i + 1][0])
    if sList[i + 1][1] - sList[i][1] > 1:
        newEnds.insert(0, sList[i][1])

newEnds = sorted(newEnds)

merged = [tuple(newEnds[i:i + 2]) for i in range(0, len(newEnds) - 1, 2)]

print(merged)
"""
"""
Alright, it works in limited cases. I have to improve it so it works in more cases if not all. The key to seeing if a tuple fits inside another completely is if its first number is greater than or equal to the first number of some other interval and if its second number is less than or equal to the second number of that other interval.

So the key would be taking some interval and comparing it to others. So something like the sorted list of tuples [(3, 6), (5, 7), (6, 12), (10, 12), (11, 116)] I'd start with the second tuple and compare it with the first. Maybe use some nested loops of i and j.

for i in range(len(sList) - 1):
    for j in range(i + 1, len(sList) - 1):
        if sList[j][0] >= sList[i][0] and sList[j][1] <= sList[i][1]:
            del sList[j]
        elif sList[j][0] >= sList[i][0] and sList[j][1] >= sList[i][1]:
            if sList[i][1] in newEnds:
                newEnds[newEnds.index(sList[i][1])] = sList[j][1]
            else:
                newEnds.append(max(sList[j][1], sList[i][1]))
        elif sList[j][0] >= sList[i][1]:
            newEnds.append(sList[j][0])

print(sorted(list(set(newEnds))))

Ok I need to put the 12 at the index where the 7 was found. I can find the 7 with the newEnds[newEnds.index(sList[i][1])] = sList[j][1]

might be able to come up with a neater for loop by using slices.

for pair in sList:
    for tup in sList[1:]:
        if pair[0] <= tup[0] <= pair[1] and pair[0] <= tup[1] <= pair[1]:
            del tup
        elif pair[0] <= tup[0] <= pair[1] and pair[1] <= tup[1]:
            if pair[1] in newEnds:
                newEnds[newEnds.index(pair[1])] = tup[1]
            else:
                newEnds.append(max(tup[1], pair[1]))
        elif tup[0] >= pair[1]:
            newEnds.append(tup[0])

print(sorted(list(set(newEnds))))
"""

# Ok, another idea. Permanently changing list that keeps track of openings and closings. Use newEnds for this. If I were going through this as a human with common sense etc. I'd do something like this.

# Note that the smallest of numbers is in the first tuple so the numbers in it get added immediately. (tup[0] and tup[1] appended to newEnds). Then I look at the next tuple to see if it's first number is between the 3 and 6 (or [0] and [-1]). This can either be done with n in range(newEnds[0], newEnds[-1]) or newEnds[0] <= n <= newEnds[-1]. Maybe I should use -2 instead. Just in acknowledgement of changing conditions which always have at least 2 numbers though.

# If it is between the numbers the loop should *skip it and* move on. The next number to compare is tup[1]. Since 7 is not between 3 and 6, the loop should compare 6 to see if it's between 5 and 7 (or tup[0] and tup[1]). If it is, the 7 or tup[1] should become the new end.

# Unless the first number in a tuple is greater than the last number in the previous, it's never going to be added. If tup[0] is in fact greater than newEnds[-1] then the tuple should be appended to newEnds. It will become the new newEnds[-1] and newEnds[-2]. The cycle continues from there.


lis = [()]
sList = sorted(lis)
newEnds, merged = [], []
newEnds.extend((sList[0][0], sList[0][1]))

for pair in sList[1:]:
    if newEnds[-2] <= pair[0] <= newEnds[-1]:
        if newEnds[-2] <= pair[1] <= newEnds[-1]:
            continue
        else:
            newEnds[-1] = pair[1]
    elif pair[0] > newEnds[-1]:
        newEnds.extend((pair[0], pair[1]))

merged = [tuple(newEnds[i:i + 2]) for i in range(0, len(newEnds) - 1, 2)]

print(merged)


# Wow, that (the above) worked perfectly! Now to just finish it off with that list comprehension and be done with it forever.
