with open('input.txt') as f:
    adapters = f.readlines()
adapters = [int(x.strip()) for x in adapters]

adapters.sort()

#part 1
def part1(ls):
    ls.insert(0, 0)
    vol1 = 0
    vol3 = 1
    for i in range(len(ls)-1):
        if ls[i+1]-ls[i] == 1:
            vol1+=1
        elif ls[i+1]-ls[i] == 3:
            vol3+=1
    return [vol1, vol3]

part1Result = part1(adapters)
print(part1Result[0]*part1Result[1])

#part 2
def isvalid(ls):
    for i in range(len(ls)-1):
        if ls[i+1]-ls[i] not in [1, 2, 3]:
            return False

    return True

adapters.append(adapters[-1]+3)

possiblefound = [adapters]
possibleBuffer = []
possiblenew = [adapters]
counter = 0
while True:
    flag = 0
    for pos in possiblenew:
        for i in range(1, len(pos)-1):
            new = list(pos)
            del new[i]
            if isvalid(new):
                if new not in possiblefound:
                    possiblefound.append(new)
                    possibleBuffer.append(new)
                    counter +=1
                    flag = 1
    
    possiblenew = []
    possiblenew = list(possibleBuffer)
    possibleBuffer = []
    print(len(possiblefound))
    if flag == 0:
        break

print(len(possiblefound))

 