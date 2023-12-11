import numpy as np

sum = 0
with open("data.txt") as f:
    for line in f:
        arrays = []
        array = np.array(line.split(" ")).astype(int)
        arrays.append(array)
        while np.any(array):
            array = np.diff(array)

            arrays.append(array)

        current_value = 0
        for array in arrays[::-1][1:]:
            first_element = array[0]
            current_value = first_element - current_value
        sum += current_value

print(sum)