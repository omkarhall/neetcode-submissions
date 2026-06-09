class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
            # 1 1 2
            #
            nums.sort()
            res = []
            def backtrack(i, subset):
                if i == len(nums):
                    res.append(subset.copy())
                    return
                subset.append(nums[i])
                backtrack(i+1,subset)
                i += 1
                while i < len(nums) and nums[i] == nums[i-1]:
                    i += 1
                subset.pop()
                backtrack(i, subset)
            if nums:
                backtrack(0, [])
            return res