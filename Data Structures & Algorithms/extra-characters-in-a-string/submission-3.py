class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            cur = self.root
            for ch in w:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.endOfWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        memo = {len(s): 0}
        trie = Trie(dictionary).root

        def dfs(i):
            if i in memo:
                return memo[i]
            res = 1 + dfs(i+1)
            cur = trie
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.endOfWord:
                    res = min(res, dfs(j+1))
            memo[i] = res
            return memo[i]
        return dfs(0)