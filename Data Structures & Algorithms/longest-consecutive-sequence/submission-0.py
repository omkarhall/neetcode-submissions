class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxL = 0
        for n in nums:
            cur = 0
            if n-1 not in s:
                m = n
                while m in s:
                    cur += 1
                    m = m+1
                    maxL = max(cur, maxL)
        return maxL
