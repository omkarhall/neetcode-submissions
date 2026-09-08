class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        memo = {}
        def dfs(r, c):
            if r == ROWS - 1:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            res = 0
            for nc in range(COLS):
                res = max(res, dfs(r+1, nc) + points[r+1][nc] - abs(nc - c))
            memo[(r, c)] = res
            return res
        
        res = 0
        for c in range(COLS):
            res = max(res, points[0][c] + dfs(0, c))
        return res
            