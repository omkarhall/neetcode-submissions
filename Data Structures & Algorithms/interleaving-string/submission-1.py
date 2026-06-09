class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        dfs(i, j) represents whether s3 0...(i+j) is formed by interleaving 
                    s1 0...i and s2 0...j
        
            if i + j == len(s3):
                return True        
            res = False
            if i < len(s1) and s3[i + j] == s1[i]:
                res = res or dfs(i + 1, j)
            if j < len(s2) and s3[i + j] == s2[j]:
                res = res or dfs(i, j + 1)
            return res
        '''
        memo = {}
        def dfs(i, j):
            if i + j == len(s3):
                if i == len(s1) and j == len(s2):
                    return True   
                return False  
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = False
            if i < len(s1) and s3[i + j] == s1[i]:
                memo[(i, j)] = memo[(i, j)] or dfs(i + 1, j)
            if j < len(s2) and s3[i + j] == s2[j]:
                memo[(i, j)] = memo[(i, j)] or dfs(i, j + 1)
            return memo[(i, j)]
        return dfs(0, 0)



            