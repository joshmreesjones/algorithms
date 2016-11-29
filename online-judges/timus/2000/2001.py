input1 = [int(n) for n in input().split()]
input2 = [int(n) for n in input().split()]
input3 = [int(n) for n in input().split()]

a1, b1 = input1[0], input1[1]
a2, b2 = input2[0], input2[1]
a3, b3 = input3[0], input3[1]

weight1 = a3
weight2 = b2

print("%d %d" % (a1 - weight1, b1 - weight2))
