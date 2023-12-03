data = []

with open("data.txt") as f:
    for line in f:
        data.append(line.strip())

def is_near(x, y1, y2, data) -> bool:
    has_near = False
    for i in range(x-1, min(x+2, len(data))):
        for j in range(y1-1, min(y2+2, len(data[i]))):
            if data[i][j] != "." and not data[i][j].isnumeric():
                has_near = True
    return has_near

start_index, end_index = -1, -1
current_number = 0

summe = 0

for line_index,line in enumerate(data):
    if start_index != -1:
        if is_near(line_index - 1, start_index, end_index, data):
            summe += current_number

        start_index, current_number = -1, 0 

    for char_index, char in enumerate(line):
        if char.isnumeric():
            if start_index == -1:
                start_index = char_index
            
            end_index = char_index
            current_number = current_number * 10 + int(char)
        
        elif start_index != -1:
            if is_near(line_index, start_index, end_index, data):
                summe += current_number
            start_index, current_number = -1, 0

print(summe)