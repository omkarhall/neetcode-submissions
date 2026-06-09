class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def minOpers(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = 0
            if word1[i] == word2[j]:
                memo[(i, j)] = minOpers(i+1, j+1)
            else:
                memo[(i, j)] = 1 + min(minOpers(i, j + 1), minOpers(i + 1, j), minOpers(i + 1, j + 1))
            return memo[(i, j)]
        return minOpers(0, 0)