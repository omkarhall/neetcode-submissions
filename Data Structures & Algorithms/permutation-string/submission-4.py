class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Freq = [0] * 26
        s2Freq = [0] * 26
        for i in range(len(s1)):
            s1Freq[ord(s1[i]) - ord('a')] += 1
            s2Freq[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Freq[i] == s2Freq[i]:
                matches += 1
        
        l = 0
        r = len(s1)
        while r < len(s2):
            if matches == 26:
                return True

            i = ord(s2[r]) - ord('a')
            s2Freq[i] += 1
            if s1Freq[i] == s2Freq[i]:
                matches += 1
            elif s1Freq[i] + 1 == s2Freq[i]:
                matches -= 1
            
            i = ord(s2[l]) - ord('a')
            s2Freq[i] -= 1
            if s1Freq[i] == s2Freq[i]:
                matches += 1
            elif s1Freq[i] - 1 == s2Freq[i]:
                matches -= 1
            l += 1
            r += 1
        
        return True if matches == 26 else False
