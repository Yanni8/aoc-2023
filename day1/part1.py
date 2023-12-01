import re

sum = 0

PATTERN = re.compile(r"(\d)")

with open('data.txt', 'r') as f:
    for line in f:
        matches = re.findall(PATTERN, line)
        sum += int(matches[0]) * 10 + int(matches[-1])

print(f"Solution: {sum}")