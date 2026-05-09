class Solution:
    def minAdd(self, s):
        open_count = close_needed = 0

        for c in s:
            if c == '(':
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                close_needed += 1

        return open_count + close_needed
