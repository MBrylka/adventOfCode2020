def isValidSledRental(line):
    boundaries = line[0].split('-')
    character = line[1]
    password = line[2]
    
    count = password.count(character)
    
    if(count >= int(boundaries[0]) and count <= int(boundaries[1])):
        return True
    
    return False

def isValidToboggan(line):
    positions = line[0].split('-')
    character = line[1]
    password = line[2]

    size = len(password)

    posA = int(positions[0])
    posB = int(positions[1])

    if((password[posA-1] == character) ^ (password[posB-1] == character)):
        return True
    return False


with open('input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
lines = [x.replace(':', '') for x in lines]
lines = [x.split(' ') for x in lines]

countValid = 0
for line in lines:
    if isValidToboggan(line):
        countValid += 1

print(countValid)