class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        
        for ch in t:
            if ch not in d:
                return False
            else:
                d[ch] -= 1
        
        for ch in d:
            if d[ch] != 0:
                return False
        return True