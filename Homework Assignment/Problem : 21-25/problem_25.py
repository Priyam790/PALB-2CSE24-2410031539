class Solution:
    def arr_palindrome(self, arr):
        return all(str(x) == str(x)[::-1] for x in arr)
