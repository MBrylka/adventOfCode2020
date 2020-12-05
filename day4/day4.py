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


print(validPassports1)