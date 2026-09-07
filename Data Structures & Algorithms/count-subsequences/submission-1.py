class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        memo = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == t[j]:
                memo[(i, j)] = dfs(i+1, j) + dfs(i+1,j+1)
            else:
                memo[(i, j)] = dfs(i+1,j)
            return memo[(i, j)]
        return dfs(0, 0)
        '''
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][len(t)] = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]