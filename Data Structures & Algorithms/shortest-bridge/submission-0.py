class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dirs = [[0, 1], [0, -1], [1,0], [-1, 0]]
        def dfs(r, c):
            if r < 0 or r >= N or c < 0 or c >= N or grid[r][c] != 1:
                return
            q.append((r, c))
            grid[r][c] = 2
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
        
        q = deque()
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break
            if q:
                break
        
        d = 0
        while q:
            level_size = len(q)
            for i in range(level_size):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] == 1:
                            return d
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            d += 1

