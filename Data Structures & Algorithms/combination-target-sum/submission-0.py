class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def helper(i, curSum):
            if curSum > target or i >= len(nums):
                return
            if curSum == target:
                res.append(temp.copy())
                return
            
            temp.append(nums[i])
            helper(i, curSum+nums[i])
            
            temp.pop()
            helper(i+1, curSum)

        helper(0, 0)
        return res