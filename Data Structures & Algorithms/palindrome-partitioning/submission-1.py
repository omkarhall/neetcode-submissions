class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        part = []
        def dfs(i, j):
            if j >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if isPalindrome(s, i, j):
                part.append(s[i : j + 1])
                dfs(j+1, j+1)
                part.pop()
            
            dfs(i, j+1)
        dfs(0, 0)
        return res

            
        
