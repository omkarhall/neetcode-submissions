class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, combo, sum_):
            if sum_ == target:
                res.append(combo[:])
                return
            if i >= len(nums) or sum_ > target:
                return
            combo.append(nums[i])
            dfs(i, combo, sum_ + nums[i])
            combo.pop()
            dfs(i + 1, combo, sum_)
        res = []
        dfs(0, [], 0)
        return res