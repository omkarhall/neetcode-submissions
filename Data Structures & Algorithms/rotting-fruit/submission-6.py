class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque() 
        fresh = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in dirs:
                    if 0 <= r+dr < ROWS and 0 <= c+dc < COLS and grid[r+dr][c+dc] == 1:
                        grid[r+dr][c+dc] = 2
                        q.append((r+dr,c+dc))
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1