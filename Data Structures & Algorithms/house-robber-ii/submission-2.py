class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        arr1 = nums[1:]
        arr1[-2] = max(arr1[-2], arr1[-1])
        for i in range(len(arr1)-3, -1,-1):
            arr1[i] = max(arr1[i+1], arr1[i] + arr1[i+2])
            print(arr1[i])
        
        arr2 = nums[:-1]
        arr2[-2] = max(arr2[-2], arr2[-1])
        for i in range(len(arr2)-3, -1,-1):
            arr2[i] = max(arr2[i+1], arr2[i] + arr2[i+2])

        return max(arr1[0],arr2[0])