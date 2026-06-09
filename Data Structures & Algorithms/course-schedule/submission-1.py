class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if not adjList[course]:
                return True
            
            visiting.add(course)
            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            #adjList[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True