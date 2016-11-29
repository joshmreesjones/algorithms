# 2.1-2
# Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.

def insertion_sort_descending(array):
    for j in range(0, len(array)):
        data = array[j]
        i = j - 1
        while i >= 0 and data > array[i]:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = data

A = [31, 41, 59, 26, 41, 58]
insertion_sort_descending(A)
print(A) # prints [59, 58, 41, 41, 31, 26]
