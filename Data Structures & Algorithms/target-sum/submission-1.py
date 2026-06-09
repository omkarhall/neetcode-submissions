class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(i, amt):
            if (i, amt) in memo:
                return memo[(i, amt)]
            if i == len(nums) and amt == target:
                return 1
            if i == len(nums) and amt != target:
                return 0
            memo[(i, amt)] = backtrack(i+1, amt+nums[i]) + backtrack(i+1, amt-nums[i])
            return memo[(i, amt)]
        return backtrack(0,0)