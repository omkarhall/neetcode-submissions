class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def helper(i):
            if i > len(nums)-1:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(helper(i+1), helper(i+2) + nums[i])
            return memo[i]
        
        return helper(0)