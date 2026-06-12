class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        memo = {}
        def _canPartition(i, target):
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False
            if (i, target) in memo:
                return memo[(i, target)]
            memo[(i, target)] = _canPartition(i + 1, target - nums[i]) or _canPartition(i + 1, target)
            return memo[(i, target)]
        return _canPartition(0, sum(nums) / 2)