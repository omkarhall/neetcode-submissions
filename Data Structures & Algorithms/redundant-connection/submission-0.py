class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = {i : [] for i in range(n + 1)}
        indegree = [0] * (n + 1)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            indegree[node] -= 1
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append(nei)

        for i in range(len(edges) - 1, -1, -1):
            u, v = edges[i]
            if indegree[u] > 0 and indegree[v] > 0:
                return [u, v]
        return []

