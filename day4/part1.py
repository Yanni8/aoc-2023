points = 0

with open("data.txt") as f:
    for line in f:
        line = line.removeprefix("Card 1:")

        wining, have = line.split("|")
        wining = wining.strip().split(" ")
        have = have.strip().split(" ")

        current_points = 0
        for num in have:
            if num == "":
                continue
            if num in wining:
                print("Num: ", num)
                if current_points == 0:
                    current_points = 1
                else:
                    current_points *= 2
        points += current_points

print(points)