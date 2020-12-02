with open('input.txt') as f:
    lines = f.readlines()
lines = [int(x.strip()) for x in lines]

i = 0
j = 0
k = 0
while i < len(lines):
    j = i+1
    while j < len(lines):
        k = j+1
        while k < len(lines):
            if(lines[i]+lines[j]+lines[k] == 2020):
                print(lines[i], lines[j], lines[k], lines[i]*lines[j]*lines[k])
                break
            k+=1
        j+=1
    i+=1

