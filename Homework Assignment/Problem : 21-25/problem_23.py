class Solution:
    def threeWayPartition(self, arr, a, b):
        lo, mid, hi = 0, 0, len(arr) - 1

        while mid <= hi:
            if arr[mid] < a:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo += 1; mid += 1
            elif arr[mid] <= b:
                mid += 1
            else:
                arr[mid], arr[hi] = arr[hi], arr[mid]
                hi -= 1
