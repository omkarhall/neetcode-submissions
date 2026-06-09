class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        
        for ch in t:
            d[ch] -= 1

        for ch in d:
            if d[ch] != 0:
                return False
        return True