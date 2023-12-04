def get_points(wining, have) -> int:
    points = 0
    for num in have:
        if num == "":
            continue
        if num in wining:
            points += 1
    return points

multiplier = {}
MAX_CARD_NUMBER = 0

with open("data.txt") as f:
    for line in f:
        
        card_number, line = line.split(":")
        card_number = int(card_number.removeprefix("Card "))
        
        wining, have = line.split("|")
        wining = wining.strip().split(" ")
        have = have.strip().split(" ")
        
        
        points = get_points(wining, have)

        for i in range(card_number+1, card_number + points + 1):
            multiplier[i] = multiplier.get(i, 0) + 1 * (multiplier.get(card_number, 0) + 1)    

        MAX_CARD_NUMBER = card_number

points = 0

for i in range(1, MAX_CARD_NUMBER+1):
    points += multiplier.get(i, 0) + 1

print(f"Solution of Part 2 Day 4: {points}")