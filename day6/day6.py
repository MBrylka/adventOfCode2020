with open('input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
groups = []
group = []
for line in lines:
    if line != '':
        group.append(line)
    else:
        groups.append(group)
        group = []
groups.append(group)

total = 0
total2 = 0
for group in groups:
    #part1
    groupped = ''.join(group)
    sum = list(dict.fromkeys(groupped))
    total += len(sum)

    #part2
    sets = []
    for g in group:
        sets.append(set([x for x in g]))
    intersection = sets[0].intersection(*sets)
    sum = len(intersection)
    total2 += sum

print(total)
print(total2)        
