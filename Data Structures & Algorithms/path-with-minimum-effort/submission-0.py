class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        pq = [[0, 0, 0]] # diff, r, c
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while pq:
            diff, r, c = heapq.heappop(pq)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (ROWS - 1, COLS - 1):
                return diff
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(pq, [newDiff, nr, nc])