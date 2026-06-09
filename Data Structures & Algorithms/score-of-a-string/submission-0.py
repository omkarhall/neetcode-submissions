class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            score += abs(int(ord(s[i]) - int(ord(s[i+1]))))
        return score