class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
                return True
        max_ = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if isPalindrome(i, j):
                    if j - i + 1 > len(max_):
                        max_ = s[i:j+1]
        return max_
        '''
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
