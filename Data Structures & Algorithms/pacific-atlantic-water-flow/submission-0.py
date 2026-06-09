class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(r, c, reachable):
            reachable.add((r,c))
            
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                row, col= r+dr, c+dc
                if (row in range(rows) and 
                    col in range(cols) and
                    (row, col) not in reachable and
                    heights[row][col] >= heights[r][c]):
                    dfs(row, col, reachable)

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
