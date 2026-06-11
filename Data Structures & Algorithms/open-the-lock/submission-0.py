class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        q = deque(["0000"])
        visited = set(deadends)
        visited.add("0000")
        dist = 0
        while q:
            lenQ = len(q)
            for _ in range(lenQ):
                lock = q.popleft()
                if lock == target:
                    return dist
                for nei in children(lock):
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            dist += 1
        return -1

