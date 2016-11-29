def merge(a, b):
    i, j, result = 0, 0, []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result

def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        halfway = len(a) // 2
        left = merge_sort(a[:halfway])
        right = merge_sort(a[halfway:])
        return merge(left, right)

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
    print(merge_sort(test))
