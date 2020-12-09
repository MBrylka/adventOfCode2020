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

    def contains(self, name):
        for con in self.contents:
            if con[0] == name:
                return True
        return False

    def getContents(self):
        return self.contents

Bags = []
#preparing data
for bag in bags:
    name = bag[0] + ' ' + bag[1]
    b = None
    b = Bag(name)

    size = (len(bag)-2)//3
    containing = ''
    for i in range(size):
        containing = bag[3+(i*3)]+' '+bag[4+(i*3)]
        quantity = bag[2+(i*3)]
        b.addContent(containing, quantity)
    Bags.append(b)
    print(b)
