class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        numCount = {n: 0 for n in nums}
        for n in nums:
            numCount[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy()) 
                return
            for n in numCount:
                if numCount[n] > 0:
                    perm.append(n)
                    numCount[n] -= 1
                    dfs()
                    numCount[n] += 1
                    perm.pop()
        dfs()
        return res
