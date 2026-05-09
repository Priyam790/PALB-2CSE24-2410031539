class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        min_len = float('inf')
        left, curr_sum = 0, 0

        for right in range(n):

            curr_sum += arr[right]    # expand window by moving right

            # shrink from left as long as sum still exceeds x
            while curr_sum > x:
                min_len = min(min_len, right - left + 1)
                curr_sum -= arr[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
