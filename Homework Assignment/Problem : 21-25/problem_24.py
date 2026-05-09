class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        # window size = count of elements <= k
        window = sum(1 for x in arr if x <= k)
        
        # count good elements in first window
        good = sum(1 for i in range(window) if arr[i] <= k)
        max_good = good
        
        # slide the window
        for i in range(1, n - window + 1):
            if arr[i - 1] <= k: good -= 1
            if arr[i + window - 1] <= k: good += 1
            max_good = max(max_good, good)
        
        # swaps needed = bad elements inside best window
        return window - max_good
