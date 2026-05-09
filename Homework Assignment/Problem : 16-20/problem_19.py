from collections import Counter

class Solution:
    def isSubset(self, a, b):

        # Step 1: Build frequency map for array a[]
        freq = Counter(a)

        # Step 2: Check each element of b[] against the map
        for x in b:
            if freq[x] == 0:
                return False   # not found or exhausted
            freq[x] -= 1        # consume one occurrence

        return True
