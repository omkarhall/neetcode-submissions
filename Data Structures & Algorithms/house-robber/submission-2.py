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
        
        arr = [0] * len(nums)
        arr[-1] = nums[-1]
        arr[-2] = max(nums[-1], nums[-2])
        for i in range(len(arr)-3, -1,-1):
            arr[i] = max(arr[i+1], nums[i] + arr[i+2])
        return arr[0]
