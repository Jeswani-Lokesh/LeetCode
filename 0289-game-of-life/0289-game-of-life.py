class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        # Encode state in 2 bits:
        #   bit 0 (current & 1) = OLD state
        #   bit 1 (current & 2) = NEW state
        # This lets us read old while writing new.
        
        for i in range(m):
            for j in range(n):
                # Count live neighbors using the OLD state (bit 0)
                live = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            live += board[ni][nj] & 1   # read old bit
                
                # Apply rules; set bit 1 if the cell is alive next gen
                if board[i][j] & 1:  # currently live
                    if live == 2 or live == 3:
                        board[i][j] |= 2   # stays alive
                else:                # currently dead
                    if live == 3:
                        board[i][j] |= 2   # becomes alive
        
        # Shift to the new state: drop old bit, keep new bit
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1