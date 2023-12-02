import re

sum = 0


with open("data.txt") as f:

    for line in f:
    
        _, content = line.split(":")
    
        limit = {"red": 0, "green": 0, "blue": 0}
    
        for game in re.split(r",|;", content):
            
            number, color = game.strip().split(" ")
            
            number = int(number)
            
            if number > limit[color]:
                limit[color] = number
        
        power = 1
        
        for color_limit in limit.values():
            power *= color_limit
        
        sum +=  power

print(sum)
