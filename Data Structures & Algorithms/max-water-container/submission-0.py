class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        maxWater = 0
        cur = 0
        while i < j:
            if heights[i] < heights[j]:
                h = heights[i]
                cur = (j-i) * h
                maxWater = max(maxWater, cur)
                i += 1
            else:
                h = heights[j]
                cur = (j-i) * h
                maxWater = max(maxWater, cur)
                j -= 1
        return maxWater
