class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(i, combo, sum_):
            if sum_ == target:
                res.append(combo.copy())
                return
            if sum_ > target:
                return
            if i == len(candidates):
                return
            combo.append(candidates[i])
            backtrack(i + 1, combo, sum_ + candidates[i])
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            combo.pop()
            backtrack(i, combo, sum_)

        if candidates:
            backtrack(0, [], 0)
        return res