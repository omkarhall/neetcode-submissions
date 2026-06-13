class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        while 1:
            stack = []
            collisions = 0
            for i in range(len(asteroids)):
                if stack:
                    if asteroids[i] < 0 and stack[-1] > 0:
                        if abs(asteroids[i]) > stack[-1]:
                            stack.pop()
                            stack.append(asteroids[i])
                        elif abs(asteroids[i]) == stack[-1]:
                            stack.pop()
                        collisions += 1
                    else:
                        stack.append(asteroids[i])
                else:
                    stack.append(asteroids[i])
            asteroids = stack
            if collisions == 0:
                return stack
        return []
