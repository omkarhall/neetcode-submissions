class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        marked = set()
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(r, c):
            marked.add((r,c))
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if (row in range(rows) and
                    col in range(cols) and
                    (row, col) not in marked and
                    board[row][col] == "O"):
                    dfs(row,col)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols-1] == "O":
                dfs(r, cols-1)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows-1][c] == "O":
                dfs(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in marked:
                    board[r][c] = "X"