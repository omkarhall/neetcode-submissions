class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        pre[1] = nums[0]
        for i in range(2, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        
        suf = [0] * len(nums)
        suf[-2] = nums[-1]
        for i in range(len(nums)-3, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        
        prod = [0] * len(nums)
        prod[0] = suf[0]
        prod[-1] = pre[-1]
        for i in range(1, len(nums)-1):
            prod[i] = pre[i] * suf[i]
        return prod
