import heapq

class Solution:
    def minOps(self, arr):
        total = sum(arr)
        target = total / 2
        ops = 0

        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)

        while total > target:
            largest = -heapq.heappop(max_heap)
            halved = largest / 2
            total -= halved
            heapq.heappush(max_heap, -halved)
            ops += 1

        return ops
