class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            alive = True
            while stack and alive and asteroids[i] < 0 and stack[-1] > 0:
                if abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                elif abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(asteroids[i])
        return stack
