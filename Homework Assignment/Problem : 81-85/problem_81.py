class Solution:
    def minSwaps(self, s1, s2):
        # count mismatches: (0,1) and (1,0)
        a = b = 0
        for c1, c2 in zip(s1, s2):
            if c1 == '0' and c2 == '1': a += 1
            elif c1 == '1' and c2 == '0': b += 1

        # total 1s and 0s must be equal across both strings
        if (a + b) % 2 != 0: return -1

        # each pair (0,1)+(0,1) or (1,0)+(1,0) needs 1 swap
        # a mixed pair (0,1)+(1,0) needs 2 swaps
        return a // 2 + b // 2 + 2 * (a % 2)
