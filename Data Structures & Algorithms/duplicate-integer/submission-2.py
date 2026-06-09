class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                if d[n] == 1:
                    return True
                d[n] += 1
        return False

            