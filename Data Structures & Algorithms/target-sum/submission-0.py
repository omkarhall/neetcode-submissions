class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, amt):
            if i == len(nums) and amt == target:
                return 1
            if i == len(nums) and amt != target:
                return 0
            return backtrack(i+1, amt+nums[i]) + backtrack(i+1, amt-nums[i])
        return backtrack(0,0)