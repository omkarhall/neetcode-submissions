class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def backtrack(i, target):
            if (i, target) in memo:
                return memo[(i, target)]
            if target == 0:
                return 0
            if i == len(coins) and target == 0:
                return 0
            if i == len(coins) and target != 0:
                return float('inf')
            if target < 0:
                return float('inf')

            memo[(i, target)] = min(backtrack(i + 1, target), backtrack(i, target - coins[i]) + 1)
            return memo[(i, target)]
        res = backtrack(0, amount)
        return res if res < float('inf') else -1
        