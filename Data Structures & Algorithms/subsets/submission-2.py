class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(subset, i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            helper(subset, i + 1)
            subset.pop()
            helper(subset, i + 1)
        helper([], 0)
        return res