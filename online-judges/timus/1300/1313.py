n = int(input())

display = []
for i in range(n):
    display.append([p for p in input().split(' ')])

result = []
for i in range(2*n - 1):
    row = i if i < n else n - 1
    column = 0 if i < n else i - (n - 1)

    while (row >= 0 and column < n):
        result.append(display[row][column])

        row -= 1
        column += 1

print(' '.join(result))
