class Solution:
    def tribonacci(self, n: int) -> int:
        '''
        memo = {}
        def dfs(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = dfs(n-1) + dfs(n-2) + dfs(n-3)
            return memo[n]
        return dfs(n)
        '''
        if n <= 2:
            return 1 if n != 0 else 0
        memo = [0] * (n+1)
        memo[1] = 1
        memo[2] = 1
        c1 = 0 # n-3
        c2 = 1 # n-2
        c3 = 1 # n-1
        for i in range(3, n+1):
            tmp1, tmp2 = c2, c3
            c3 = c3 + c2 + c1
            c1 = tmp1
            c2 = tmp2
            #memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        #return memo[n]
        return c3