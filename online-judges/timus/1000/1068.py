n = int(input())

dx = 1 if n >= 1 else -1

i = 1
sum = 1
while (i != n):
    i += dx
    sum += i

print(sum)
