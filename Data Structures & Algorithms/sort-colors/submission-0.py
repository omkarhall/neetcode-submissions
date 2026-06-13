class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3
        for n in nums:
            buckets[n] += 1
        for i in range(len(nums)):
            if buckets[0] > 0:
                nums[i] = 0
                buckets[0] -= 1
            elif buckets[1] > 0:
                nums[i] = 1
                buckets[1] -= 1
            elif buckets[2] > 0:
                nums[i] = 2
                buckets[2] -= 1

            
        
            