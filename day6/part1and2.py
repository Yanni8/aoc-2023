with open("data.txt") as f:
    times = f.readline().removeprefix("Time: ").strip()
    distances = f.readline().removeprefix("Distance: ").strip()

sum = 1

for time, distance in zip(times.split(), distances.split()):
    time, distance = int(time), int(distance)
    combinations = 0
    for i in range(0, time):
        if (time - i) * i > distance:
            combinations += 1
    sum *= combinations

print(sum)