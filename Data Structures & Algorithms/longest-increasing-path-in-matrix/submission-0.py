class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        memo = {}
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            res = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[r][c] < matrix[nr][nc]:
                    res = max(res, dfs(nr, nc))
            memo[(r, c)] = res + 1
            return memo[(r, c)]
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res