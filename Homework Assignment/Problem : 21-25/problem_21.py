class Solution:
    def findMinDiff(self, arr, m):

        # Step 1: Sort the array
        arr.sort()
        n = len(arr)

        # Step 2: Slide a window of size m across the sorted array
        min_diff = float('inf')

        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]  # window max - window min
            min_diff = min(min_diff, diff)

        return min_diff
