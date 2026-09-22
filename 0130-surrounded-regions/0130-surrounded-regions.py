class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """Modify board in place."""
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        
        def dfs(r, c):
            # Stop at bounds or any non-'O' cell
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != "O":
                return
            board[r][c] = "S"          # mark as Safe (border-connected)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # 1. Launch DFS from every 'O' on the four borders
        for r in range(m):
            dfs(r, 0)                  # left column
            dfs(r, n - 1)              # right column
        for c in range(n):
            dfs(0, c)                  # top row
            dfs(m - 1, c)              # bottom row
        
        # 2. Flip: surrounded 'O' → 'X', safe 'S' → 'O'
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"  # not reached from border → captured
                elif board[r][c] == "S":
                    board[r][c] = "O"  # restore the safe ones
