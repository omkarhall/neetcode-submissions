class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i: [] for i in range(1, n+1)}
        for u, v, t in times:
            adjList[u].append([v, t])
        pq = [(0, k)]
        visited = set()
        while pq:
            t, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return t
            for nei, nei_t in adjList[node]:
                heapq.heappush(pq, [nei_t + t, nei])
        return -1
