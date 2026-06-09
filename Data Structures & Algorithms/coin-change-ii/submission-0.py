class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, curAmt):
            if curAmt > amount:
                return 0
            if i == len(coins):
                if curAmt == amount:
                    return 1
                return 0
            if (i, curAmt) in memo:
                return memo[(i, curAmt)]
            memo[(i, curAmt)] = dfs(i, curAmt + coins[i]) + dfs(i + 1, curAmt)
            return memo[(i, curAmt)]
        
        return dfs(0, 0)
