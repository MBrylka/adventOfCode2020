import time

with open('input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

#clearing data
bags = []
for line in lines:
    line = line.replace(' bags', '')
    line = line.replace(' bag', '')
    line = line.replace(' contain', '')
    line = line.replace(',', '')
    line = line.replace('.', '')
    #if 'no other' not in line:
    bags.append(line.split(' '))


class Bag:
    name = ''
    contents = []
    def __init__(self, name):
        self.name = name

    def addContent(self, name, quantity):
        self.contents.append([name, quantity])

    def contains(self, name)
        for con in self.contents:
            if con[0] == name:
                return True
        return False

    def getContents(self, name):
        for con in self.contents:
            if con[0] == name:
                return con



#preparing data
preparedBags = []
for bag in bags:
    name = bag[0] + ' ' + bag[1]
    size = (len(bag)-2)//3
    containing = ''
    preparedBag = [name]
    for i in range(size):
        containing = bag[3+(i*3)]+' '+bag[4+(i*3)]
        preparedBag.append(containing)
        preparedBag.append(bag[2+(i*3)])
    #if(preparedBag[0] != 'shiny gold'):
        preparedBags.append(preparedBag)
    
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return len(lst3) > 0

#searching
#part 1
preparedBagsOriginal = preparedBags
preparedBags2 = []
for b in preparedBags:
    if(b[0] != 'shiny gold'):
        print(b)
        preparedBags2. append(b)
preparedBags = preparedBags2 #awful, needs refactoring
counter = 0
toSearch = ['shiny gold']
newToSearch = []
while len(toSearch) > 0:
    for prepared in preparedBags:
        if intersection(toSearch, prepared[1:]):
            counter+=1
            newToSearch.append(prepared[0])

    toSearch = list(set(newToSearch))
    
    newToSearch = []
    preparedCopy = []
    for prepared in preparedBags:
        if prepared[0] not in toSearch:
            preparedCopy.append(prepared)
    
    preparedBags = preparedCopy
    print(toSearch)

print(counter)
#part 2

'''
counter = 0
toSearch = ['shiny gold']
newToSearch = []
preparedBags = preparedBagsOriginal
while len(toSearch) > 0:
    for prepared in preparedBags:
        print(prepared[0])
        if prepared[0] in toSearch:
            print('found')
            for x in range(1, (len(prepared)-1)/2):
                print(prepared[x], prepared[x+1])
        
'''