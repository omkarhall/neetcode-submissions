class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r,c,visited,prevH):
            if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]) or (r,c) in visited or heights[r][c] < prevH:
                return
            visited.add((r,c))
            dfs(r+1,c,visited, heights[r][c])
            dfs(r,c-1,visited, heights[r][c])
            dfs(r-1,c,visited, heights[r][c])
            dfs(r,c+1,visited, heights[r][c])



        pacific, atlantic = set(), set()
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    dfs(r,c,pacific,0)
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    dfs(r,c,atlantic,0)
        
        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        return res