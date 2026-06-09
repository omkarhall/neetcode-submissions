class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        def backtrack(i, s):
            if s == target:
                res.append(combo.copy())
                return
            if i >= len(nums) or s > target:
                return
                
            combo.append(nums[i])
            backtrack(i, s+nums[i])
            combo.pop()
            backtrack(i+1,s)
        backtrack(0,0)
        return res