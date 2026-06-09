class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1

        for i in range(len(t)):
            if t[i] in counts:
                counts[t[i]] -= 1
            else:
                return False
        
        for k, v in counts.items():
            if counts[k] != 0:
                return False
        return True
        