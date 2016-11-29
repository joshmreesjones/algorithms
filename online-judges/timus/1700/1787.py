input1 = [int(n) for n in input().split()]

rate = input1[0]
minutes = input1[1]
cars = [int(n) for n in input().split()]

i = 0
line = 0
while i < minutes:
    line += cars[i]

    if line <= rate:
        line = 0
    else:
        line -= rate

    i += 1

print(line)
