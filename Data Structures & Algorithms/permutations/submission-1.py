class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        def backtrack(chosen):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not chosen[i]:
                    perm.append(nums[i])
                    chosen[i] = True
                    backtrack(chosen)
                    perm.pop()
                    chosen[i] = False
        backtrack([False] * len(nums))
        return res
