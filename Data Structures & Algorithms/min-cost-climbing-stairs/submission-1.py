class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        def helper(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = min(helper(i+1), helper(i+2)) + cost[i]
            return memo[i]
        return min(helper(0), helper(1))
    