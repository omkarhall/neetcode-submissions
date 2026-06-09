class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])
        
        minLR = [0] * n
        for i in range(n):
            minLR[i] = min(maxLeft[i], maxRight[i])
        water = 0
        for i in range(n):
            if minLR[i] - height[i] > 0:
                water += minLR[i] - height[i]
        return water
            

