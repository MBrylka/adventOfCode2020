from copy import copy, deepcopy

with open('input.txt') as f:
    rows = f.readlines()
rows = [x.strip() for x in rows]

def splitString(word): 
    return [char for char in word]  


map = []
map2 = []

for row in rows:
    a = [char for char in row]
    map.append(list(a))

map2 = deepcopy(map)

def printMap(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end = '')
        print()

def mapsTheSame(m, m2):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != m2[i][j]:
                return False
    return True

while True:
    for i in range(len(map)):
        for j in range(len(map[0])):

            sx = i-1 if i > 0 else i
            ex = i+1 if i < len(map)-1 else i

            sy = j-1 if j > 0 else j
            ey = j+1 if j < len(map[0])-1 else j

            counter = 0
            
            for x in range(sx, ex+1):
                for y in range(sy, ey+1):
                    if x != i or y != j:
                        if map[x][y] == '#': 
                            counter+=1
            if map[i][j] == 'L' and counter == 0:
                map2[i][j] = '#'
            if map[i][j] == '#' and counter >= 4:
                map2[i][j] = 'L'
    if mapsTheSame(map, map2):
        break
    map = deepcopy(map2)

count = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '#':
            count+=1

print(count)