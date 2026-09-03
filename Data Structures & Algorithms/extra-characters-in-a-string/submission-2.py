class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        '''
        words = set(dictionary)
        memo = {}
        def dfs(i, j):
            if j == len(s):
                return j - i
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i:j+1] in words:
                memo[(i, j)] = min(dfs(i, j+1), dfs(j+1, j+1))
            else:
                memo[(i, j)] = min(dfs(i, j+1), 1 + dfs(i+1, i+1))
            return memo[(i, j)]
        return dfs(0, 0)
        '''
        words = set(dictionary)
        dp = [[0] * (len(s)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][len(s)] = len(s) - i
        for i in range(len(s)-1,-1,-1):
            for j in range(len(s)-1,-1,-1):
                if s[i:j+1] in words:
                    dp[i][j] = min(dp[i][j+1], dp[j+1][j+1])
                else:
                    dp[i][j] = min(dp[i][j+1], 1 + dp[i+1][i+1])
        return dp[0][0]