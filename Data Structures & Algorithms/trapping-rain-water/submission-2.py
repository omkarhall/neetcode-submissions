class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        res = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                if height[l] >= maxL:
                    maxL = height[l]
                else:
                    res += maxL - height[l]
            else:
                r -= 1
                if height[r] >= maxR:
                    maxR = height[r]
                else:
                    res += maxR - height[r]
        return res

            

            

