class Solution:
    def minPersons(self, arr):
        n = len(arr)
        # max_reach[i] = farthest right index covered by anyone who can reach i
        max_reach = [-1] * n
        for i in range(n):
            if arr[i] == -1: continue
            l = max(0, i - arr[i])
            r = min(n - 1, i + arr[i])
            max_reach[l] = max(max_reach[l], r)

        count, cur_end, farthest = 0, 0, 0

        for i in range(n):
            farthest = max(farthest, max_reach[i])
            if farthest < i:        return -1   # gap — can't be covered
            if i == cur_end:
                count += 1
                cur_end = farthest
                if cur_end >= n - 1: return count

        return -1
