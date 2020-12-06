import re

with open('input.txt') as f:
    lines = f.readlines()

passports = []
passport = []
for line in lines:
    if line != '\n':
        passport.append(line)
    else:
        passports.append(passport)
        passport = []
passports.append(passport)

validPassports1 = 0
validPassports2 = 0
validation = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for passs in passports:
    elements = []
    for s in passs:
        s = s.split(' ')
        elem = []
        for x in s:
            elem = x.split(':')
            elements.append(elem)
    
    #part 1
    if(all(temp in [x[0] for x in elements] for temp in validation)):
        validPassports1 += 1
        #part 2
        invalidPass = False
        for el in elements:
            tag = el[0]
            value = el[1].strip()
            if tag == 'byr':
                pattern = re.compile('19[2-9][0-9]|200[0-2]') #1920 - 2002
                if pattern.match(value) == None:
                    invalidPass = True
            if tag == 'iyr':
                pattern = re.compile('201[0-9]|2020') #2010 - 2020
                if pattern.match(value) == None:
                    invalidPass = True
            if tag == 'eyr':
                pattern = re.compile('202[0-9]|2030') #2020 - 2030
                if pattern.match(value) == None:
                    invalidPass = True
            if tag == 'hgt':
                pattern = re.compile("(\d+(?:\.\d*)?)\s*(cm|in)") #number cm|in
                print(value, pattern.match(value)!=None)
            if tag == 'hcl':




    if not invalidPass:
        validPassports2+=1
    #print(elements)

print(validPassports1)
print(validPassports2)