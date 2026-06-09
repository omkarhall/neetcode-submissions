class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def _numDecodings(i):
            if i in memo:
                return memo[i]
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            res = _numDecodings(i + 1)
            if i < len(s) - 1:
                if s[i] == '1' or s[i] == '2' and s[i+1] in '0123456':
                    res += _numDecodings(i + 2)
            memo[i] = res
            return memo[i]
        return _numDecodings(0)