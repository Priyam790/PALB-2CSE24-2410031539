class Solution:
    def footpathConstruction(self, a, queries):
        n, m = len(a), len(a[0])
        INF = float('inf')

        # precompute corner-anchored prefix minimums
        tl = [[INF] * m for _ in range(n)]  # min of a[0..i][0..j]
        tr = [[INF] * m for _ in range(n)]  # min of a[0..i][j..m-1]
        bl = [[INF] * m for _ in range(n)]  # min of a[i..n-1][0..j]
        br = [[INF] * m for _ in range(n)]  # min of a[i..n-1][j..m-1]

        for i in range(n):
            for j in range(m):
                tl[i][j] = a[i][j]
                if i > 0: tl[i][j] = min(tl[i][j], tl[i-1][j])
                if j > 0: tl[i][j] = min(tl[i][j], tl[i][j-1])
                if i > 0 and j > 0: tl[i][j] = max(tl[i][j], min(tl[i-1][j], tl[i][j-1]))

        # simpler recompute
        tl = [[INF] * m for _ in range(n)]
        tr = [[INF] * m for _ in range(n)]
        bl = [[INF] * m for _ in range(n)]
        br = [[INF] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                tl[i][j] = a[i][j]
                if i > 0: tl[i][j] = min(tl[i][j], tl[i-1][j])
                if j > 0: tl[i][j] = min(tl[i][j], tl[i][j-1])

        for i in range(n):
            for j in range(m-1, -1, -1):
                tr[i][j] = a[i][j]
                if i > 0: tr[i][j] = min(tr[i][j], tr[i-1][j])
                if j < m-1: tr[i][j] = min(tr[i][j], tr[i][j+1])

        for i in range(n-1, -1, -1):
            for j in range(m):
                bl[i][j] = a[i][j]
                if i < n-1: bl[i][j] = min(bl[i][j], bl[i+1][j])
                if j > 0:   bl[i][j] = min(bl[i][j], bl[i][j-1])

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                br[i][j] = a[i][j]
                if i < n-1: br[i][j] = min(br[i][j], br[i+1][j])
                if j < m-1: br[i][j] = min(br[i][j], br[i][j+1])

        res = []
        for R, C in queries:
            r, c = R - 1, C - 1   # convert to 0-indexed
            total = 0
            if r > 0   and c > 0:   total += tl[r-1][c-1]
            if r > 0   and c < m-1: total += tr[r-1][c+1]
            if r < n-1 and c > 0:   total += bl[r+1][c-1]
            if r < n-1 and c < m-1: total += br[r+1][c+1]
            res.append(total)

        return res
