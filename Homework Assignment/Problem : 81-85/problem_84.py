class Solution:
    def minDifference(self, arr):
        total = 24 * 3600

        def to_sec(t):
            h, m, s = map(int, t.split(':'))
            return h * 3600 + m * 60 + s

        secs = sorted(to_sec(t) for t in arr)
        min_diff = total - secs[-1] + secs[0]  # wrap-around

        for i in range(1, len(secs)):
            min_diff = min(min_diff, secs[i] - secs[i-1])

        return min_diff
