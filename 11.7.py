def innerProd(x, y):
    return sum([x[i] * y[i] for i in range(len(x)) ])

print(innerProd([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
