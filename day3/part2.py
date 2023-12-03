data = []

with open("data.txt") as f:
    for line in f:
        data.append(line.strip())

def get_gear(x, y1, y2, data) -> tuple:
    for i in range(x-1, min(x+2, len(data))):
        for j in range(y1-1, min(y2+2, len(data[i]))):
            if data[i][j] == "*":
                return (i, j)
    return None

start_index, end_index = -1, -1
number = 0
summe = 0

possible_gears = set()
gear_to_number = {}

for line_index, line in enumerate(data):
    if start_index != -1:
        gear = get_gear(line_index - 1, start_index, end_index, data)
        
        if gear is None:
            pass
        
        elif gear in possible_gears:
            summe += gear_to_number[gear] * number
            del gear_to_number[gear]
        else:
            possible_gears.add(gear)
            gear_to_number[gear] = number

        start_index = -1 
        number = 0
    
    for char_index, char in enumerate(line):
        if char.isnumeric():
            if start_index == -1:
                start_index = char_index
            end_index = char_index
            number = number * 10 + int(char)
        elif start_index != -1:
            gear = get_gear(line_index, start_index, end_index, data)
            if gear is None:
                pass
            elif gear in possible_gears:
                summe += gear_to_number[gear] * number
                del gear_to_number[gear]
            else:
                possible_gears.add(gear)
                gear_to_number[gear] = number

            start_index = -1
            number = 0

print(summe)