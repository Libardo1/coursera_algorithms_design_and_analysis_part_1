count_inv = 0

def mergesort(A):
    n = len(A)
    if n == 1:
        return A

    m = n // 2
    
    left = mergesort(A[:m])
    right = mergesort(A[m:])

    res = []

    i, j = 0, 0
    len_l = len(left)
    len_r = len(right)

    while i < len_l and j < len_r:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            global count_inv
            count_inv += 1
            res.append(right[j])
            j += 1

    if i < len_l:
        res.extend(left[i:])
    if j < len_r:
        res.extend(right[j:])

    return res, count_inv


# print(mergesort([1]))
# print(mergesort([2, 1]))
# print(mergesort([3, 2, 1]))
# print(mergesort([3, 4, 2, 1]))

print(mergesort([2, 4, 1, 3, 5]))
