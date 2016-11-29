from itertools import zip_longest

# 2.3-5
# Referring back to the searching problem (see Exercise 2.1-3), observe that if the sequence A is sorted, we can check the midpoint of the sequence against v and eliminate half of the sequence from further consideration. The binary search algorithm repeats this procedure, halving the size of the remaining portion of the sequence each time. Write pseudocode, either iterative or recursive, for binary search. Argue that the worst-case running time of binary search is Ө(lg(n)).

# The recurrence for a binary search is:
#
# T(n) = { Θ(1)             if n = 1
#        { T(n / 2) + Θ(1)  if otherwise
#
# The solution to this recurrence is Θ(lg(n)).

def binary_search(array, key):
    if len(array) == 0: return -1

    return binary_search_helper(array, key, 0, len(array) - 1)

# This solution could be improved.
def binary_search_helper(array, key, lower, upper):
    if lower == upper:
        if array[lower] == key:
            return lower
        else:
            return -1
    elif lower + 1 == upper:
        if array[lower] == key:
            return lower
        elif array[upper] == key:
            return upper
        else:
            return -1
    else:
        midpoint = (lower + upper) // 2

        # If array[midpoint] is equal to the key, we still keep looking
        # because we still need to check if it's the first occurrence of
        # the key.
        if array[midpoint] < key:
            return binary_search_helper(array, key, midpoint, upper)
        else:
            return binary_search_helper(array, key, lower, midpoint)

# Search for 2
A = [0, 1, 2, 3, 4, 5] #  2
B = [1, 1, 2, 2, 3, 3] #  2
C = [1, 2, 2, 2, 2, 3] #  1
D = [2, 3, 3, 3, 3, 3] #  0
E = [1, 1, 1, 1, 1, 2] #  5
F = [2, 2, 2, 2, 2, 2] #  0
G = [1, 1, 1, 1, 1, 1] # -1
H = [0, 1, 3, 4, 5, 6] # -1
I = [2] #  0
J = [1] # -1
K = []  # -1

search_key = 2
tests    = [A, B, C, D, E, F,  G,  H, I,  J,  K]
expected = [2, 2, 1, 0, 5, 0, -1, -1, 0, -1, -1]

passed = True
for test, expected in zip_longest(tests, expected):
    result = binary_search(test, search_key)
    print("result: %d\texpected: %d" % (result, expected))

    if (result != expected):
        print("\tTest failed\n")
        passed = False

if passed:
    print("All tests passed.")
else:
    print("Tests failed.")
