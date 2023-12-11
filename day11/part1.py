import numpy as np

with open("data.txt") as f:
    data = np.array([[0 if char == "." else 1 for char in line.strip()] for line in f])

zero_rows = np.where(~data.any(axis=1))[0]
zero_cols = np.where(~data.any(axis=0))[0]

data = np.insert(data, zero_rows, 0, axis=0)
data = np.insert(data, zero_cols, 0, axis=1)

indexes = np.array(np.where(data == 1)).T

summe = 0

passed = set()

for i, j in indexes:
    for x, y in indexes:
        if (i, j) != (x, y) and ((i, j),(x, y)) not in passed and ((x, y),(i, j)) not in passed:
            length = abs(i - x) + abs(j - y) 
            summe += length
            passed.add(((i, j),(x, y)))

print(summe)