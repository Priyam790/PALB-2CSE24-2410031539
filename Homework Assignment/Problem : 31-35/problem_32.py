class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, curr, remaining):
            if remaining == 0:
                res.append(list(curr))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                curr.append(candidates[i])
                backtrack(i, curr, remaining - candidates[i])
                curr.pop()

        candidates.sort()
        backtrack(0, [], target)
        return res
