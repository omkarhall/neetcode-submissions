class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = 0 # s
        r = 0 # t
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                r += 1
            l += 1
        return len(t) - r