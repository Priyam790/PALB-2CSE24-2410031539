class Solution:
    def median(self, arr):
        arr.sort()
        n = len(arr)
        mid = n // 2
        return arr[mid] if n % 2 != 0 else (arr[mid - 1] + arr[mid]) / 2
