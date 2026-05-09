class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(start, curr, remaining):
            if remaining == 0:
                res.append(list(curr))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue                          # skip duplicates
                curr.append(candidates[i])
                backtrack(i + 1, curr, remaining - candidates[i])
                curr.pop()

        backtrack(0, [], target)
        return res
