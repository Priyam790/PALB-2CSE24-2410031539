class Solution:
    def leftSmaller(self, arr):
        res, stack = [], []

        for x in arr:
            while stack and stack[-1] >= x:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(x)

        return res
