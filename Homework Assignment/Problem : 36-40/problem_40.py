class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, curr):
            res.append(list(curr))
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return res
