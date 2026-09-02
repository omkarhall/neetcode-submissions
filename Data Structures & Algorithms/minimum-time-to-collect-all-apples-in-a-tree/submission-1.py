class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node, par):
            time = 0
            for nei in adjList[node]:
                if nei == par:
                    continue
                nei_time = dfs(nei, node)
                if nei_time > 0 or hasApple[nei]:
                    time += 2 + nei_time
            return time
        res = dfs(0, -1)
        return res