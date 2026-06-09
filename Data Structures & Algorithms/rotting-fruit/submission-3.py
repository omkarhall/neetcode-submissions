class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        seconds = 0

        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and 
                        col in range(cols) and 
                        (row, col) not in visited and 
                        grid[row][col] == 1):
                        q.append((row,col))
                        visited.add((row,col))
                        grid[row][col] = 2
                        fresh -= 1
            seconds += 1
        
        return seconds if fresh == 0 else -1


        