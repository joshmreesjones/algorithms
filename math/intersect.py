# Given two intervals [a, b] and [c, d], determine whether they intersect.

def intersect(a, b, x, y):
    # [a, b] and [x, y] do not intersect in two cases:
    # - when [a, b] is strictly before [x, y]: b < x
    # - when [x, y] is strictly before [a, b]: y < a
    # Nonintersection occurs when (b < x or y < a), so
    # intersection occurs when not (b < x or y < a).
    return not (b < x or y < a)

tests = [
    (0, 1, 2, 3, False),
    (0, 1, 1, 2, True),
    (0, 2, 1, 3, True),
    (0, 2, 0, 3, True),
    (1, 2, 0, 3, True),
    (0, 2, 1, 2, True),
    (0, 1, 0, 1, True),
    (1, 2, 0, 2, True),
    (0, 3, 1, 2, True),
    (0, 2, 0, 1, True),
    (1, 3, 0, 2, True),
    (1, 2, 0, 1, True),
    (2, 3, 0, 1, False)
]

for a, b, x, y, expected in tests: assert intersect(a, b, x, y) == expected
print("Tests passed.")
