
with open('input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

height = len(lines)
width = len(lines[0])
def listTree(w, h):
    y = 0
    x = 0
    trees = 0
    while y < height-1:
        x +=w 
        y+=h
        if(x > width-1):
            x = x-width
        print(lines[y])
        if(lines[y][x] == '#'):
            trees += 1
    return trees

config = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

multiply = 1
for con in config:
    multiply *= listTree(con[0], con[1])

print(multiply)