class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1

        q = deque(["0000"])
        visited = set(deadends)
        visited.add("0000")

        dist = 0
        while q:
            qLen = len(q)
            for _ in range(qLen):
                lock = q.popleft()
                if lock == target:
                    return dist
                for i in range(4):
                    nei = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:]
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                    nei = lock[:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i+1:]
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            dist += 1
        return -1
                    
