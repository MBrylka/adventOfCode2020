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
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def contains(self, searchNames):
        ret = []
        for c in self.contents:
            ret.append(c[0])
        s1 = set(ret)
        s2 = set(searchNames)
        if s1.intersection(s2):
            return True
        return False
        
    def getContents(self):
        return self.contents
    
    def getName(self):
        return self.name

Bags = []
BagsOriginal = []
#preparing data
for bag in bags:
    name = bag[0]+' '+bag[1]
    contents = []
    
    bagsize = (len(bag)-2)//3
    for i in range(bagsize):
        contents.append([bag[3+i*3]+' '+bag[4+i*3], bag[2+i*3]])
    
    Bags.append(Bag(name, contents))
BagsOriginal = Bags

#part 1
toSearch = ['shiny gold']
newSearch = []
counter = 0
while len(toSearch) > 0:
    for B in Bags:
        if B.contains(toSearch):
            counter+=1
            newSearch.append(B.getName())
    toSearch = newSearch
    newSearch = []
    BagsCopy = []
    for B in Bags:
        if B.getName() not in toSearch:
            BagsCopy.append(B)

    Bags = BagsCopy
print(counter)

def countBags(toSearch):
    counter = 0 
    for B in Bags:
        if B.getName() in toSearch:
            for con in B.getContents():
                counter += int(con[1])+ int(con[1]) * countBags(con[0])     
    return counter

toSearch = ['shiny gold']
counter = countBags(toSearch)
print(counter)
    

