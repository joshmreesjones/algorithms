# 2.1-3
# Consider the searching problem:
# Input: A sequence of n numbers A = [a1, a2, ..., an] and a value v.
# Output: An index i such that v = A[i] or the special value NIL if v does not appear in A.
# Write pseudocode for linear search, which scans through the sequence, looking for v. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.

def linear_search(array, value):
    i = 0
    while i < len(array):
        if array[i] == value:
            return i
        i += 1
    return None # None is NIL

A = [31, 41, 59, 26, 41, 58]
print(linear_search(A, 59)) # prints 2
print(linear_search(A, 41)) # prints 1
print(linear_search(A, 42)) # prints None (NIL)

# Loop invariant
# At the start of each iteration of the while loop, the subarray array[0:i-1] does not contain the specified value.

# Initialization
# Initially, the subarray is empty, therefore it cannot contain the specified value.

# Maintenance
# In the body of the while loop, we test to see if the element array[i] is equal to the specified value. If it is not, we increment i, thus adding to the subarray an element not equal to the specified value, and preserving the loop invariant. If it is, we return the value i, which is correct.

# Termination
# When the while loop terminates, the value of i is equal to the length of the array. The subarray is now array[0:length of array - 1], which is the entire array. In this case, we return None (NIL), which is correct because the array does not contain the specified value.
