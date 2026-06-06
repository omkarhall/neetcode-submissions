class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        max_ = float('-inf')
        for i in range(len(nums)):
            cur = 1
            for j in range(i, len(nums)):
                cur *= nums[j]
                max_ = max(max_, cur)
        return max_
        '''
        res = max(nums)
        curMin, curMax = 1, 1
        for i in range(0, len(nums)):
            temp = nums[i] * curMax
            curMax = max(nums[i] * curMax, nums[i] * curMin, nums[i])
            curMin = min(temp, nums[i] * curMin, nums[i])
            res = max(res, curMax)
        return res