seeds = []
seed_to_location = []
seed_to = []

with open("data.txt") as f:
    start = []
    end = []
    num_range = []

    for line in f:
        if line.startswith("seeds:"):
            seeds = line.removeprefix("seeds:").strip().split(" ")
            seeds = [int(i) for i in seeds]
        elif ":" in line:
            start = []
            end = []
            num_range = []
        elif line == "\n":
            if start == []:
                continue
            seed_to.append((start, end, num_range))
        else:
            destination, source, _range = line.strip().split(" ")
            destination, source, _range = int(destination), int(source), int(_range)
            start.append(source)
            end.append(destination)
            num_range.append(_range)
    seed_to.append((start, end, num_range))

for starts, ends, ranges in seed_to:
    new_seeds = []
    for seed in seeds:
        found = False
        for start, end, _range in zip(starts, ends, ranges):
            if 0 <= (seed - start) < _range:
                new_seeds.append(end + (seed - start))
                found = True
        if not found:
            new_seeds.append(seed)
    seeds = new_seeds

print(min(seeds))
