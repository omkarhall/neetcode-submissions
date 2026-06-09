class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        canSegment(i, j) represents whether s 0...j can be segmented into dict words
            w/ current segment being s[i...j] (i and j inclusive)
        base case
        j >= n -> False
        j == n - 1
            s[i...j] in Dict -> True
            else -> False

        recursive case
            if s[i...j+1] in wordDict:
                canSegment(j + 1, j + 1) or canSegment(i, j + 1)
            else
                canSegment(i, j + 1)
        '''
        wordSet = set(wordDict)
        n = len(s)
        memo = {}
        def canSegment(i, j):
            if j >= n:
                return False
            if j == n - 1:
                if s[i:j+1] in wordSet:
                    return True
                return False
            if (i, j) in memo:
                return memo[(i, j)]
            res = canSegment(i, j + 1)
            if s[i:j+1] in wordDict:
                res = res or canSegment(j + 1, j + 1)
            memo[(i, j)] = res
            return memo[(i, j)]
            
        return canSegment(0, 0)