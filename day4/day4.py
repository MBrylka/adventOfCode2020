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

validPassports = 0
validation = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for passs in passports:
    elements = []
    for s in passs:
        s = s.split(' ')
        elem = []
        for x in s:
            elem.append(x[0:x.find(':')])
        elements += elem
    print(elements)
    if(all(temp in elements for temp in validation)):
        validPassports += 1

print(validPassports)