'''
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
'''    

'''
Klasa?

Lista nazw, jesli zawiera shiny gold to ją oznacz i pozniej szukaj po tej nazwie i usun ja z tablicy az do skutku
'''


with open('input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

bags = []
for line in lines:
    line = line.replace(' bags', '')
    line = line.replace(' bag', '')
    line = line.replace(' contain', '')
    if 'no other' not in line:
        bags.append(line.split(' '))

print(bags)