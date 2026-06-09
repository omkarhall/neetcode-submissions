class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        def dfs(i,j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            return dfs(i+1, j) + dfs(i-1,j) + dfs(i, j-1) + dfs(i,j+1)
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == 1:
                    res += dfs(i,j)
        return res