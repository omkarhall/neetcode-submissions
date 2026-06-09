class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        for ch in s1:
            s1_freq[ch] += 1
        
        i = 0
        while i + len(s1) <= len(s2):
            s2_freq = defaultdict(int)
            cur = 0
            for j in range(i, i+len(s1)):
                s2_freq[s2[j]] += 1
                if s1_freq.get(s2[j], 0) < s2_freq[s2[j]]:
                    break
                elif s2_freq[s2[j]] == s1_freq.get(s2[j], 0):
                    cur += 1
                if cur == len(s1_freq):
                    return True
            i += 1
        return False
