class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def helper(i, prev):
            if i >= len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            if nums[i] > prev:
                memo[(i, prev)] = max(1 + helper(i+1, nums[i]), helper(i+1,prev))
            else:
                memo[(i, prev)] = helper(i+1, prev)
            return memo[(i, prev)] 
        return helper(0, -1e9)