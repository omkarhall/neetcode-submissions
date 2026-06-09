class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        
        def addCell(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in visited or grid[i][j] == -1:
                return
            visited.add((i,j))
            q.append((i,j))


        dist = 0
        while q:
            l = len(q)
            for i in range(l):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            dist += 1