class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        windowSum = 0
        l = 0
        r = 0
        res = 0
        while r < len(arr):
            windowSum += arr[r]
            if r - l + 1 == k:
                if windowSum / k >= threshold:
                    res += 1
                windowSum -= arr[l]
                l += 1
            r += 1
        return res
