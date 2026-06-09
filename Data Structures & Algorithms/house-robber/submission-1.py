class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        choice: skip house or rob house
        if rob house i -> move to house i + 2
        if skip house i -> move to house i + 1
        max(rob, skip)
        
        def helper(i, money):
            if i >= len(nums):
                return money
            return max(helper(i+1, money), helper(i+2, money+nums[i]))
        return helper(0,0)
        """
        if len(nums) <= 2:
            return max(nums)
        
        for i in range(len(nums)-3, -1,-1):
            nums[i] = max(nums[i+1], nums[i] + nums[i+2])
        return nums[0]
