class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        
        def mark(r,c):
            if (r in range(rows) and 
                c in range(cols) and 
                (r,c) not in visited and 
                grid[r][c] == 1):
                q.append((r,c))
                visited.add((r,c))
                grid[r][c] = 2


        seconds = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                
                mark(r+1, c)
                mark(r-1, c)
                mark(r, c+1)
                mark(r, c-1)
            seconds += 1
        if seconds != 0:
            seconds -= 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return seconds


        