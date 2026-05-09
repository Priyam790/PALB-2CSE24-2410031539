import bisect

class Solution:
    def median(self, mat):
        n, m = len(mat), len(mat[0])
        desired = (n * m + 1) // 2

        lo, hi = 1, 10**9

        while lo <= hi:
            mid = (lo + hi) // 2
            # count elements <= mid across all rows
            count = sum(bisect.bisect_right(row, mid) for row in mat)
            if count < desired: lo = mid + 1
            else:               hi = mid - 1

        return lo
