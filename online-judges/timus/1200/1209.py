index = int(input())
positions = []

for i in range(index):
    positions.append(int(input()))

# i(n) = n(n - 1) / 2
# 2i = n^2 - n
# n^2 - n + 2i
# 1 += sqrt(1 - 8i)
# ---------------------
#       2

def i(x):
    return x * (x - 1) / 2 + 1

def getDigit(position):
    n = 0
    lower = 0
    upper = 
    while True:
        if i(n) >= position - 1:
            if i(n) == position - 1:
                return '1'
            else:
                return '0'
            break
        
        n += 1

result = []

for position in positions:
    result.append(getDigit(position))

print(" ".join(result))
