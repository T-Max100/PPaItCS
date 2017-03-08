def intervalMerge(lis):
    """
    The function intervalMerge(...) takes in a list of tuples and returns a list of ordered tuples merged where the originals overlapped.

    Ex.
    >>> intervalMerge([(1,3) (4,5) (1,2) (2,3)])
    [(1,3) (4,5)]
    """

    if len(lis) <= 1:
        return lis

    orderedTuples = sorted(lis)
    newEnds, merged = [], []
    newEnds.extend((orderedTuples[0][0], orderedTuples[0][1]))

    for pair in orderedTuples[1:]:
        if newEnds[-2] <= pair[0] <= newEnds[-1]:
            if newEnds[-2] <= pair[1] <= newEnds[-1]:
                continue
            else:
                newEnds[-1] = pair[1]
        elif pair[0] > newEnds[-1]:
            newEnds.extend((pair[0], pair[1]))

    merged = [tuple(newEnds[i:i + 2]) for i in range(0, len(newEnds) - 1, 2)]

    return merged

print(intervalMerge([()]))
