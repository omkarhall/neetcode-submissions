class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))
            area = 1
            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        queue.append((r,c))
                        visited.add((r,c))
                        area += 1
            return area
        
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea


