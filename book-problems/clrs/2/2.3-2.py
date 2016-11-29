# 2.3-2
# Rewrite the MERGE procedure so that it does not use sentinels, instead stopping once either array L or R has had all its elements copied back to A and then copying the remainder of the other array back into A.
def merge(list1, list2):
    length = len(list1) + len(list2)
    result = []

    i = 0
    j = 0

    for k in range(length):
        if i >= len(list1) or j >= len(list2):
            # we've reached the end of one of the lists
            break

        # add the smaller element of the two locations
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # copy remaining elements to result
    if i >= len(list1):
        result += list2[j:]
    elif j >= len(list2):
        result += list1[i:]

    return result

print(merge([1, 2, 3], [4, 5, 6]))
print(merge([2, 4, 6], [1, 3, 5]))
print(merge([1, 2, 6], [3, 4, 5]))
