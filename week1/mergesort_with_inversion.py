def mergesort(A):
    n = len(A)
    if n == 1:
        return A, 0

    m = n // 2
    
    left, count_inv_l = mergesort(A[:m])
    right, count_inv_r = mergesort(A[m:])

    count_inv = count_inv_l + count_inv_r

    res = []

    i, j = 0, 0
    len_l = len(left)
    len_r = len(right)

    while i < len_l and j < len_r:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            count_inv += len_l - i
            res.append(right[j])
            j += 1

    if i < len_l:
        res.extend(left[i:])
    if j < len_r:
        res.extend(right[j:])

    return res, count_inv


# for i in [
#         [1],
#         [2, 1],
#         [3, 2, 1],
#         [3, 4, 2, 1],
#         [2, 4, 1, 3, 5]]:
#     print(i)
#     print(mergesort(i))
#     print()

with open('IntegerArray.txt') as inf:
    numbers = [int(line) for line in inf]
