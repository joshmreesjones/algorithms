# 2.1-4
# Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in an (n + 1)-element array C. State the problem formally and write pseudocode for adding the two integers.
# Input: two n-element arrays A and B which represent one binary number each.
# Output: one (n + 1)-element array C which represents the binary addition of A and B.

def binary_add(num1, num2):
    assert len(num1) == len(num2)

    result = [0 for i in range(len(num1) + 1)]
    i = len(num1) - 1

    while (i >= 0):
        digit_sum = num1[i] + num2[i]

        result[i + 1] += digit_sum % 2
        result[i] += digit_sum // 2

        i -= 1
    
    return result

#   0000    1010    0001    1101
# + 1111  + 0101  + 1000  + 1110
# ------  ------  ------  ------
#   1111    1111    1001   11011

# 0 + 0 = 0 = 00
# 0 + 1 = 1 = 01
# 1 + 1 = 2 = 10

a = [0, 0, 0, 0]
b = [1, 1, 1, 1]

c = [1, 0, 1, 0]
d = [0, 1, 0, 1]

e = [0, 0, 0, 1]
f = [1, 0, 0, 0]

g = [1, 1, 0, 1]
h = [1, 1, 1, 0]

print(binary_add(a, b)) # prints [0, 1, 1, 1, 1]
print(binary_add(c, d)) # prints [0, 1, 1, 1, 1]
print(binary_add(e, f)) # prints [0, 1, 0, 0, 1]
print(binary_add(g, h)) # prints [1, 1, 0, 1, 1]
