class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        for ch in s1:
            s1_freq[ch] += 1
        
        i = 0
        while i + len(s1) <= len(s2):
            s2_freq = defaultdict(int)
            for j in range(i, i+len(s1)):
                s2_freq[s2[j]] += 1
                if s1_freq == s2_freq:
                    return True
            i += 1
        return False
