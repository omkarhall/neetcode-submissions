class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        i = 0
        j = 0
        maxLen = 0
        while j < len(s):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            maxLen = max(maxLen, j - i + 1)
            chars.add(s[j])
            j += 1
        return maxLen
