class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.addWord(word)
        res = set()
        def dfs(r, c, node, word):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == "#" or board[r][c] not in node.children:
                return

            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
            tmp = board[r][c]
            board[r][c] = "#"
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            board[r][c] = tmp
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")
        return list(res)