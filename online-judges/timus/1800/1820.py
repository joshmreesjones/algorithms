import math

numbers = [int(num) for num in input().split()]

n = numbers[0]
k = numbers[1]
total = 2 * n

if n <= k:
    print(2)
else:
    print(math.ceil(total / k))
