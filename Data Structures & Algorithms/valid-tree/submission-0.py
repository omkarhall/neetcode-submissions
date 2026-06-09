class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
