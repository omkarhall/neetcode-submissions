class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            if not stack:
                stack.append([(p, s)])
            else:
                topP, topS = stack[-1][0]
                topT = (target - topP) / topS
                curT = (target - p) / s
                if curT <= topT:
                    stack[-1].append((p,s))
                else:
                    stack.append([(p,s)])
        return len(stack)
