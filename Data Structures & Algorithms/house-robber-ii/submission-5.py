class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        def maxRob(i) is maximum amt robbed while robbing houses 1...i

        base case i >= n -> return 0

        return max(maxRob(i + 2) + nums[i], maxRob(i + 1))
        try from starting at house 0...n-1 and 1...n and take max
        '''
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = {}
        def maxRob(i, end):
            if i >= end:
                return 0
            if (i, end) in dp:
                return dp[(i, end)]
            dp[(i, end)] = max(maxRob(i + 2, end) + nums[i], maxRob(i + 1, end))
            return dp[(i, end)]
        
        return max(maxRob(0, len(nums)-1), maxRob(1, len(nums)))