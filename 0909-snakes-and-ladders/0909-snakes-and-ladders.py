class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # Function to convert square number to (row, col)
        def get_position(square):
            # Convert square number to row index
            row = (square - 1) // n

            # Convert square number to column index
            col = (square - 1) % n

            # Reverse row because numbering starts from bottom
            row = n - 1 - row

            # Reverse column for zig-zag pattern
            if ((n - 1 - row) % 2) == 1:
                col = n - 1 - col

            return row, col

        # Queue for BFS: (current square, number of moves)
        queue = deque()
        queue.append((1, 0))

        # Set to keep track of visited squares
        visited = set()
        visited.add(1)

        # BFS loop
        while queue:
            square, moves = queue.popleft()

            # If we reached the last square
            if square == n * n:
                return moves

            # Try all dice rolls (1 to 6)
            for i in range(1, 7):
                next_square = square + i

                # Skip if beyond board
                if next_square > n * n:
                    continue

                # Get board position
                r, c = get_position(next_square)

                # If there is a snake or ladder
                if board[r][c] != -1:
                    next_square = board[r][c]

                # If not visited, add to queue
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        # If we cannot reach the end
        return -1
        