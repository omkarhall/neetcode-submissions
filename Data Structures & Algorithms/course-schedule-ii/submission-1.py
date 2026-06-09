class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses
        res = []

        def dfs(crs):
            state = states[crs]
            if state == visiting:
                return False
            elif state == visited:
                return True
            states[crs] = visiting
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            states[crs] = visited
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
