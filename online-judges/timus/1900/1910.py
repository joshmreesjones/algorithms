segments = int(input())
forces = [int(n) for n in input().split()]

maxSum = forces[0] + forces[1] + forces[2]
maxIndex = 1
for i in range(1, segments - 2):
    sum3 = forces[i] + forces[i + 1] + forces[i + 2]
    if sum3 > maxSum:
        maxSum = sum3
        maxIndex = i + 1

print("%d %d" % (maxSum, maxIndex + 1))
