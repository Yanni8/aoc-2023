import re

sum = 0

PATTERN = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
 
number_to_int = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def to_num(s: str) -> int:
    number = number_to_int.get(s, -1)
    if number == -1:
        return int(s)
    return number

with open('data.txt', 'r') as f:
    for line in f:
        matches = re.findall(PATTERN, line)
        sum += to_num(matches[0]) * 10 + to_num(matches[-1])

print(f"Solution: {sum}")