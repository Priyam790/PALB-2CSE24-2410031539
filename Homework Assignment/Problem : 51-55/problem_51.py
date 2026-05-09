class Solution:
    def sumQuery(self, a, q, query):
        n, m = len(a), len(a[0])

        # build 2D prefix sum
        pre = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                pre[i][j] = (a[i-1][j-1] + pre[i-1][j]
                             + pre[i][j-1] - pre[i-1][j-1])

        res = []
        for r1, c1, r2, c2 in query:
            total = (pre[r2+1][c2+1] - pre[r1][c2+1]
                     - pre[r2+1][c1] + pre[r1][c1])
            res.append(total)

        return res
