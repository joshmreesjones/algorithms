def qsort(array):
    if array:
        pivot = array.pop() # Use the last element as the pivot
        smaller = [n for n in array if n <= pivot]
        bigger  = [n for n in array if n  > pivot]
        return qsort(smaller) + [pivot] + qsort(bigger)
    else:
        return array

def q(a):return q([n for n in a if n <= a[-1]])+[a[-1]]+q([n for n in a if n > a[-1]]) if a else a
