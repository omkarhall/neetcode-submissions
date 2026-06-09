class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(i, temp):
            if i >= len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[i])
            helper(i + 1, temp)
            x = temp.pop()
            while (i < len(nums) and nums[i] == x):
                i += 1
            helper(i, temp)

        helper(0, [])
        return res