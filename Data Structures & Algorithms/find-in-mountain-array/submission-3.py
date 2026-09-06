class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # binary search for the peak
        l = 0
        r = mountainArr.length() - 1
        peak = -1
        while l <= r:
            mid = (l + r) // 2
            if mountainArr.get(mid-1) < mountainArr.get(mid) > mountainArr.get(mid+1):
                peak = mid
                break
            elif mountainArr.get(mid-1) < mountainArr.get(mid):
                l = mid + 1
            else:
                r = mid - 1

        l = 0
        r = peak
        while l <= r:
            mid = (l + r) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l = peak + 1
        r = mountainArr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
