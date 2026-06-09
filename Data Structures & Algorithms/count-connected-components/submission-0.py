class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res