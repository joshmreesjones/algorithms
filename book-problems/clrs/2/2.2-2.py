# 2.2-2
# Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the element in A[1]. The find the second smallest element of A, and exchange it with A[2]. Continue in this manner for the first n - 1 elements of A. Write pseudocode for this algorithm, which is known as a selection sort. What loop invariant does this algorithm maintain? Why does it need to run for only the first n - 1 elements, rather than for all n elements? Give the best-case and worst-case running times of selection sort in Θ-notation.

def selection_sort(array):
    i = 0
    while (i < len(array) - 1):
        # find the index of the smallest number
        j = smallest_index = i
        while (j < len(array)):
            if array[j] < array[smallest_index]:
                smallest_index = j
            j += 1
        # swap array[i] and array[smallest_index]
        smallest = array[smallest_index]
        array[smallest_index] = array[i]
        array[i] = smallest
        i += 1

A = [31, 41, 59, 26, 41, 58]
selection_sort(A)
print(A) # prints [26, 31, 41, 41, 58, 59]

# Loop invariant: at the start of each iteration of the outer while loop, the subarray array[0:i] contains sorted elements which are all less than or equal to all elements in the subarray array[i:n].
# The outer while loop only needs to run for the first n - 1 elements because of the loop invariant: the subarray array[0:n-1] contains elements which are all less than or equal to the subarray array[n-1:n], so the array is sorted.

# Best-case running time: (1) + (n) + (n - 1) + (sum (i=0..n-2) n - i + 1) + (sum (i=0..n-2) n - i) + (n - 1) + (sum (i=0..n-2) n - i + 1) + (n - 1) + (n - 1) + (n - 1) + (n - 1)
# This should simplify to Θ(n^2).

# Worst-case running time: (1) + (n) + (n - 1) + (sum (i=0..n-2) n - i + 1) + (sum (i=0..n-2) n - i) + (sum (i=0..n-2) n - i + 1) + (sum (i=0..n-2) n - i + 1) + (n - 1) + (n - 1) + (n - 1) + (n - 1)
# This should also simplify to Θ(n^2).
