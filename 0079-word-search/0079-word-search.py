class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        
        def dfs(r, c, idx):
            # All characters matched → found it
            if idx == len(word):
                return True
            # Out of bounds, or char mismatch → dead end
            if (r < 0 or r >= m or c < 0 or c >= n
                    or board[r][c] != word[idx]):
                return False
            
            # Mark current cell as visited (choose)
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore the 4 neighbors
            found = (dfs(r + 1, c, idx + 1) or
                     dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or
                     dfs(r, c - 1, idx + 1))
            
            # Restore the cell (un-choose / backtrack)
            board[r][c] = temp
            
            return found
        
        # Try starting the search from every cell
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False