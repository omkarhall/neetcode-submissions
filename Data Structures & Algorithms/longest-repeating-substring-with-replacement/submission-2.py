class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = defaultdict(int)
        mostFreq = 0
        l = 0
        res = 0
        for r in range(len(s)):
            m[s[r]] += 1
            mostFreq = max(mostFreq, m[s[r]])
            while (r - l + 1 - mostFreq > k):
                m[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res