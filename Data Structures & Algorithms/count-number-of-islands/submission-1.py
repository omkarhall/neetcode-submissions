class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in dirs:
                grid[i][j] = "0"
                if 0 <= i + dr < len(grid) and 0 <= j + dc < len(grid[0]) and grid[i+dr][j+dc] == "1":
                    dfs(i+dr, j+dc)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        return count

        
