class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        maxWater = 0
        cur = 0
        while i < j:
            cur = (j-i) * min(heights[i], heights[j])
            maxWater = max(maxWater, cur)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxWater
