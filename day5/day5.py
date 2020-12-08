with open('input.txt') as f:
    bpasses = f.readlines()
bpasses = [x.strip() for x in bpasses]

seats = []

seats = []
for bpass in bpasses:
    bpass = bpass.replace('F', '0')
    bpass = bpass.replace('B', '1')
    bpass = bpass.replace('L', '0')
    bpass = bpass.replace('R', '1')
    seats.append([bpass[:7], bpass[7:]])

maxId = 0

listOfSeats = []
for a in range(0,128):
    for b in range(0, 8):
        listOfSeats.append(a*8+b)

for seat in seats:
    row = int(seat[0], 2)
    col = int(seat[1], 2)
    seatId = row * 8 + col
    if seatId > maxId:
        maxId = seatId
    listOfSeats.remove(seatId)
urSeat = 0
for i in range(1, len(listOfSeats)-1):
    if listOfSeats[i]-1 != listOfSeats[i-1] and listOfSeats[i]+1 != listOfSeats[i+1]:
        urSeat=listOfSeats[i]
print(urSeat)
print(maxId)