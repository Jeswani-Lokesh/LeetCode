class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Count rows
        rows = len(grid)

        # Count columns
        cols = len(grid[0])

        # Queue stores rotten oranges
        queue = deque()

        # Count fresh oranges
        fresh = 0

        # Scan the grid first
        for r in range(rows):
            # Scan each column
            for c in range(cols):
                # If orange is rotten
                if grid[r][c] == 2:
                    # Add it as a BFS starting point
                    queue.append((r, c))

                # If orange is fresh
                elif grid[r][c] == 1:
                    # Count it
                    fresh += 1

        # If no fresh oranges exist
        if fresh == 0:
            return 0

        # Track minutes
        minutes = 0

        # Four movement directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS while rotten oranges can spread
        while queue and fresh > 0:
            # Number of rotten oranges at current minute
            level_size = len(queue)

            # Process all oranges for this minute
            for _ in range(level_size):
                # Get current rotten orange
                r, c = queue.popleft()

                # Try all directions
                for dr, dc in directions:
                    # New row
                    nr = r + dr

                    # New column
                    nc = c + dc

                    # Skip out-of-bounds cells
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    # If neighbor is fresh
                    if grid[nr][nc] == 1:
                        # Make it rotten
                        grid[nr][nc] = 2

                        # One less fresh orange
                        fresh -= 1

                        # Add newly rotten orange to queue
                        queue.append((nr, nc))

            # One BFS level finished, so one minute passed
            minutes += 1

        # If all oranges rotted
        if fresh == 0:
            return minutes

        # Some fresh oranges were unreachable
        return -1
        