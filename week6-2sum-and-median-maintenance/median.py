import copy
import heapq

# http://stackoverflow.com/questions/33024215/built-in-max-heap-api-in-python
# There is no _heappush_max in heapq, so implement one
def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)


left_heap = []                   # to keep the half smallest numbers
right_heap = []                  # to keep the half largest numbers

medians = []
medians_sum = 0
cmed = None                     # current median

with open('Median.txt') as inf:
    for k, i in enumerate(inf):
        i = int(i)
        if k == 0:
            largest_in_left = smallest_in_right = i
            _heappush_max(left_heap, i)
            cmed = i
        else:
            if i <= cmed:
                _heappush_max(left_heap, i)
            else:
                heapq.heappush(right_heap, i)

            # if the size of the two heap differ by two, move elements to
            # rebalance
            if len(left_heap) - len(right_heap) == 2:
                node = heapq._heappop_max(left_heap)
                heapq.heappush(right_heap, node)
            elif len(right_heap) - len(left_heap) == 2:
                node = heapq.heappop(right_heap)
                _heappush_max(left_heap, node)

            if len(left_heap) >= len(right_heap):
                cmed = heapq._heappop_max(left_heap)
                # put it back
                _heappush_max(left_heap, cmed)
            else:
                cmed = heapq.heappop(right_heap)
                heapq.heappush(right_heap, cmed)

        medians_sum += cmed
        medians.append(cmed)

# print(medians)
print(medians_sum % 10000)
