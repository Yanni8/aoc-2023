import numpy as np


index = 0

def to_index(x):
    global index
    if x == 1:
        index += 1
        return index
    return 0

with open("data.txt") as f:
    data = np.array([[0 if char == "." else 1 for char in line.strip()] for line in f])

zero_rows = np.where(~data.any(axis=1))[0]
zero_cols = np.where(~data.any(axis=0))[0]

data = np.insert(data, zero_rows, 0, axis=0)
data = np.insert(data, zero_cols, 0, axis=1)

data = np.asmatrix(data)

data = np.vectorize(to_index)(data)


indexes = set()

for idx in range(1, index + 1):
    i, j = np.where(data == idx)
    indexes.add((i[0], j[0]))   


summe = 0

passed = set()

for i, j in indexes:
    for x, y in indexes:
        if (i, j) != (x, y) and ((i, j),(x, y)) not in passed and ((x, y),(i, j)) not in passed:
            length = abs(i - x) + abs(j - y) 
            summe += length
            passed.add(((i, j),(x, y)))

print(summe)