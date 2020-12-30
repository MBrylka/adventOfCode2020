with open('input.txt') as f:
    lines = f.readlines()
lines = [int(x.strip()) for x in lines]

def checkSum(array, number):
    retVal = False
    for a in array:
        for b in array:
            if a != b and (a + b) == number:
                retVal = True
                break
                
    return retVal

def getWrongNumber(lines, preambSize):
    iter = 0
    size = len(lines)
    for iter in range(preambSize, size):
        if checkSum(lines[iter-preambSize:iter], lines[iter]) == False:
            return lines[iter]

def findWeakness(lines, wrongNumber):
    iter = 0
    size = len(lines)

    while iter < size:
        iter2 = iter
        sum = 0
        min = lines[iter]
        max = 0
        while iter2 < size:
            sum += lines[iter2]
            max = lines[iter2] if lines[iter2] > max else max
            iter2+=1
            if sum == wrongNumber:
                return min+max

            if sum > wrongNumber:
                break
        iter+=1




wrongNumber = getWrongNumber(lines, 25)
print(wrongNumber)

weakness = findWeakness(lines, wrongNumber)
print(weakness)