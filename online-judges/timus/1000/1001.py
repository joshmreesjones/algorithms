import sys
from math import sqrt

numbers = []
for line in sys.stdin:
    for word in line.split():
        numbers.append(word)

for n in reversed(numbers):
    print("%.4f" % sqrt(int(n)))
