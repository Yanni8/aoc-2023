import re

sum = 0

limit = {
    "red": 12,
    "green":  13,
    "blue": 14
}

with open("data.txt") as f:

    for line in f:
        id, content = line.split(":")
        
        imposible = False

        for game in re.split(r",|;", content):
            number, color = game.strip().split(" ")
            if int(number) > limit[color]:
                imposible = True

        if not imposible:
            sum += int(id.split(" ")[-1])
print(sum)