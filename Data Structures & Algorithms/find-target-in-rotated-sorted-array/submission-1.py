class Solution:
    def findMin(self, nums):
            l = 0
            r = len(nums) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= nums[-1]:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res
    
    def binarySearch(self, nums, target):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
    
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findMin(nums)
        r1 = self.binarySearch(nums[0:pivot], target)
        r2 = self.binarySearch(nums[pivot:], target) + len(nums[0:pivot])
        if r1 != -1:
            return r1
        if r2 != -1 + len(nums[0:pivot]):
            return r2
        return -1

