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
mapOriginal = deepcopy(map)
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
 
#part 2


map = deepcopy(mapOriginal)
map2 = deepcopy(map)
while True:
    for i in range(len(map)):
        for j in range(len(map[0])):
            counter = 0
            if map[i][j] != '.':
                #left
                x = i
                while x > 0:
                    x-=1
                    if map[x][j] == '#':
                        counter += 1
                        break
                    elif map[x][j] =='L':
                        break
                #right
                x = i
                while x < len(map)-1:
                    x+=1
                    if map[x][j] == '#':
                        counter += 1
                        break
                    elif map[x][j] =='L':
                        break
                #up
                y = j
                while y > 0:
                    y-=1
                    if map[i][y] == '#':
                        counter += 1
                        break
                    elif map[i][y] == 'L':
                        break
                #down
                y = j
                while y < len(map[0])-1:
                    y+=1
                    if map[i][y] == '#':
                        counter += 1
                        break
                    elif map[i][y] == 'L':
                        break
                #up-left
                x = i
                y = j
                while x > 0 and y > 0:
                    x-=1
                    y-=1
                    if map[x][y] == '#':
                        counter += 1
                        break
                    elif map[x][y] == 'L':
                        break
                
                #up-right
                x = i
                y = j
                while x < len(map)-1 and y > 0:
                    x+=1
                    y-=1
                    if map[x][y] == '#':
                        counter += 1
                        break
                    elif map[x][y] == 'L':
                        break
                
                #down-left
                x = i
                y = j
                while x > 0 and y < len(map[0])-1:
                    x-=1
                    y+=1
                    if map[x][y] == '#':
                        counter += 1
                        break
                    elif map[x][y] == 'L':
                        break
                
                #down-right
                x = i
                y = j
                while x < len(map)-1 and y < len(map[0])-1:
                    x+=1
                    y+=1
                    if map[x][y] == '#':
                        counter += 1
                        break
                    elif map[x][y] == 'L':
                        break
                
                if map[i][j] == 'L' and counter==0:
                    map2[i][j] = '#'
                elif map[i][j] == '#' and counter>=5:
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
                   