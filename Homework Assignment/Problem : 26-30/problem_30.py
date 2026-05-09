import bisect

class Solution:
    def rowWithMax1s(self, arr):
        n, m = len(arr), len(arr[0])
        max_ones, result = 0, -1

        for i in range(n):
            ones = m - bisect.bisect_left(arr[i], 1)
            if ones > max_ones:
                max_ones, result = ones, i

        return result
