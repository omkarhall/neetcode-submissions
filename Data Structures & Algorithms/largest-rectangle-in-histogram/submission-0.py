class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            if not stack:
                stack.append([i, h])
            else:
                if h < stack[-1][1]:
                    while stack and h < stack[-1][1]:
                        i2, h2 = stack.pop()
                        max_area = max(max_area, (i - i2) * h2)
                    stack.append([i2, h])
                else:
                    stack.append([i, h])
        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)
        return max_area
