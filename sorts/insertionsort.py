def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
    return a

tests = [
    [],
    [0],
    [1, 2, 3],
    [2, 3, 1],
    [1, 2, 1],
    [1, 0, -1],
    [7, 3, 2, 9, 8, 4, 10, 1, 6, 5]
]

for test in tests:
    print(insertion_sort(test))
