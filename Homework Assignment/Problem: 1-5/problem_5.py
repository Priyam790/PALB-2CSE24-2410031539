class Solution:
    def largest(self, arr):

        # Assume first element is the largest
        max_val = arr[0]

        # Compare with every other element
        for x in arr[1:]:
            if x > max_val:
                max_val = x    # update if a bigger value is found

        return max_val

        # One-liner alternative (uses built-in):
        # return max(arr)
