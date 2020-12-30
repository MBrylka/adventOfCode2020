from copy import deepcopy

with open('input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

instructions = []

for line in lines:
    chop = line.split(' ')
    instructions.append([chop[0], int(chop[1]), int(0)])

def checkInfLoop(array):
    accumulator = 0
    iterator = 0
    while True:
        if iterator >= len(array):
            return [False, accumulator]
        instructionObj = array[iterator]
        instruction = instructionObj[0]
        value = instructionObj[1]
        used = instructionObj[2]
        if used == 1:
            return [True, accumulator]

        array[iterator][2] = 1
        if instruction == 'nop':
            iterator += 1
        elif instruction == 'jmp':
            iterator += value
        elif instruction == 'acc':
            accumulator += value
            iterator += 1
        
print(checkInfLoop(deepcopy(instructions)))

iter = 0
for iter in range(len(instructions)):
    instructionsCopy = deepcopy(instructions)
    instruction = instructionsCopy[iter]

    if instruction[0] == 'nop':
        instructionsCopy[iter][0] = 'jmp'

    elif instruction[0] == 'jmp':
        instructionsCopy[iter][0] = 'nop'
    
    result = checkInfLoop(instructionsCopy)
    if result[0] == False:  
        print(result)
        


        
    
