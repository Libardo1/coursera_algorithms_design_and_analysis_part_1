import numpy as np


def quicksort(A, level=0, debug=False):
    """
    pure quicksort algorithm with always the first element selected as the pivot
    """
    if debug:
        print('{0}: level{1:3d}, sorting {2}'.format('#' * 10, level, A))

    if len(A) <= 1:
        return A

    pivot = A[0]
    i = 1
    for j in range(1, len(A)):
        if A[j] < pivot:
            if debug:
                print('swapping A[{0}] ({1}) & A[{2}] ({3})'.format(i, A[i], j, A[j]))
            A[i], A[j] = A[j], A[i]
            i += 1

    if debug:
        print('swapping A[{0}] ({1}) & A[{2}] ({3})'.format(0, A[0], i-1, A[i-1]))
    A[0], A[i-1] = A[i-1], A[0]

    if debug:
        level += 1

    return quicksort(A[:i - 1], level) + [A[i - 1]] + quicksort(A[i:], level)


def quicksort1(A):
    """
    added count of comparisons of elements to the pivot
    """
    if len(A) <= 1:
        return A, 0

    comp_count = len(A) - 1

    pivot = A[0]
    i = 1
    for j in range(1, len(A)):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[0], A[i-1] = A[i-1], A[0]

    left, left_c = quicksort1(A[:i - 1])
    right, right_c = quicksort1(A[i:])

    return left + [A[i-1]] + right, comp_count + left_c + right_c


def quicksort2(A):
    """
    with always the last element selected as the pivot
    """
    if len(A) <= 1:
        return A, 0

    A[0], A[-1] = A[-1], A[0]

    comp_count = len(A) - 1

    pivot = A[0]
    i = 1
    for j in range(1, len(A)):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[0], A[i-1] = A[i-1], A[0]

    left, left_c = quicksort2(A[:i - 1])
    right, right_c = quicksort2(A[i:])

    return left + [A[i-1]] + right, comp_count + left_c + right_c


def get_median(A):
    return np.median(A)


def get_middle_element(A):
    """
    If the array has odd length it should be clear what the "middle" element
    is; for an array with even length 2k, use the kth element as the "middle"
    element. So for the array 4 5 6 7, the "middle" element is the second one
    ---- 5 and not 6!
    """
    idx, b = divmod(len(A), 2)
    if b == 0:
        idx -= 1
    return A[idx], idx


def get_pivot(A):
    a = A[0]
    b, idx = get_middle_element(A)
    c = A[-1]

    m = get_median([a, b, c])
    if m == a:
        return m, 0
    elif m == b:
        return m, idx
    else:
        return m, len(A) - 1


def quicksort3(A, debug=False):
    """
    with always the median of the first, middle and last elements selected as
    the pivot
    """
    if len(A) <= 1:
        return A, 0

    pivot, idx = get_pivot(A)
    A[0], A[idx] = A[idx], A[0]

    comp_count = len(A) - 1

    pivot = A[0]
    i = 1
    for j in range(1, len(A)):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[0], A[i-1] = A[i-1], A[0]

    left, left_c = quicksort3(A[:i - 1])
    right, right_c = quicksort3(A[i:])

    return left + [A[i-1]] + right, comp_count + left_c + right_c


    return quicksort1(A)

print(quicksort3([1, 2, 3]))
print(quicksort3([3, 2, 1]))    # idx_median = 0
print(quicksort3([2, 1, 3]))    # idx_median = 1
print(quicksort3([3, 1, 2]))    # idx_median = 2
print(quicksort3([3, 10, 2, 5, 4, 1]))
print(quicksort3([3, 10, 2, 5, 11, 4, 1]))
print(quicksort3([5, 11, 4, 10]))
print(quicksort3([1, 2, 5, 4, 3]))


numbers = [int(_) for _ in open('QuickSort.txt')]
print(quicksort1(numbers[:])[1])
print(quicksort2(numbers[:])[1])
print(quicksort3(numbers[:])[1])


# 162085
# 160361
# 129100
