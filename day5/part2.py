seeds = []
seed_to_location = []
seed_to = [

]
with open("data.txt") as f:

    start = []
    end = []
    num_range = []
    for line in f:
        if line.startswith("seeds:"):
            seeds = line.removeprefix("seeds:").strip().split(" ")
            seeds = [(int(seeds[i]), int(seeds[i+1]) -1) for i in range(0, len(seeds), 2)]
        elif ":" in line:
            start = []
            end = []
            num_range = []
        elif line == "\n":
            if end == []:
                continue
            seed_to.append((start, end, num_range))
        else:
            destination, source, _range = line.strip().split(" ")
            destination, source, _range = int(destination), int(source), int(_range)
            start.append(source)
            end.append(destination)
            num_range.append(_range)
    seed_to.append((start, end, num_range))


current_seeds = []



def split_ranges(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    overlapping = None
    non_overlapping = []

    if start1 <= start2 <= end2 <= end1:
        overlapping = range2
    elif start2 < start1 < end1 < end2:
        overlapping = (start1, end1)
        non_overlapping = [(start2, start1 - 1), (end1 + 1, end2)]
    elif start2 < start1 <= end2 < end1:
        overlapping = (start1, end2)
        non_overlapping = [(start2, start1 - 1)]
    elif start1 <= start2 <= end1 <= end2:
        overlapping = (start2, end1)
        non_overlapping = [(end1 + 1, end2)]
    else:
        non_overlapping = [range2]

    return overlapping, non_overlapping    


for starts, ends, ranges in seed_to:
    new_seeds = []

    missing_seeds = [*seeds]
    for start, end, range in zip(starts, ends, ranges):
        new_missing_seeds = []
        for seed_start, seed_range in missing_seeds:
            overlaping, nonoverlaping = split_ranges((start, start + range - 1), (seed_start, seed_start + seed_range - 1))
            if overlaping:
                new_seeds.append((end + (overlaping[0] - start), overlaping[1] - overlaping[0]))
            if nonoverlaping:
                new_missing_seeds.extend([(i[0], i[1] - i[0]) for i in nonoverlaping])

                
        missing_seeds = new_missing_seeds
    new_seeds.extend(missing_seeds) 
    seeds = new_seeds
solution = []
for seed in seeds:
    solution.append(seed[0])

print(min(solution))
