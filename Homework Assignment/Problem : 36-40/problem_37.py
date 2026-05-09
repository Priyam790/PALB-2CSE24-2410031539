class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
