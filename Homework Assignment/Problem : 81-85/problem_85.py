from collections import Counter

class Solution:
    def sortByFreq(self, s):
        freq = Counter(s)
        return ''.join(c * freq[c] for c in sorted(freq, key=lambda x: (freq[x], x)))
