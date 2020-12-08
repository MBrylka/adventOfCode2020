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
            
            regex = {
                'byr': r'^(19[2-9][0-9]|200[0-2])$',
                'iyr': r'^(201[0-9]|2020)$',
                'eyr': r'^(202[0-9]|2030)$',
                'hgt': r'^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$',
                'hcl': r'^#[0-9a-f]{6}$',
                'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
                'pid': r'^\d{9}$'}
            
            if tag != 'cid':
                pattern = re.compile(regex[tag])
                if pattern.match(value) == None:
                    invalidPass = True

        if not invalidPass:
            validPassports2+=1

print(validPassports1) #part 1
print(validPassports2) #part 2