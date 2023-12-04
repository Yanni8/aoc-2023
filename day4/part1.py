total_points = 0

def get_points(wining, have) -> int:
    points = 0
    for num in have:
        if num == "":
            continue
        if num in wining:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points

with open("data.txt") as f:
    for line in f:
        line = line.removeprefix("Card 1:")

        wining, have = line.split("|")
        wining = wining.strip().split(" ")
        have = have.strip().split(" ")

        total_points += get_points(wining, have)

print(f"Solution of Part 1 Day 4: {total_points}")