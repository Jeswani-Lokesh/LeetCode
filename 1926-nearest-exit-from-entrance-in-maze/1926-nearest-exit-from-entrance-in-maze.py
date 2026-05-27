class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Number of rows in the maze
        rows = len(maze)

        # Number of columns in the maze
        cols = len(maze[0])

        # Get entrance row
        start_row = entrance[0]

        # Get entrance column
        start_col = entrance[1]

        # Queue stores row, column, and distance from entrance
        queue = deque()

        # Add entrance to queue with 0 steps
        queue.append((start_row, start_col, 0))

        # Mark entrance as visited
        maze[start_row][start_col] = "+"

        # Possible movement directions
        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        # Process cells using BFS
        while queue:
            # Remove front cell from queue
            row, col, steps = queue.popleft()

            # Try all 4 directions
            for dr, dc in directions:
                # New row after moving
                new_row = row + dr

                # New column after moving
                new_col = col + dc

                # Check if new position is outside maze
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue

                # If new position is a wall or already visited
                if maze[new_row][new_col] == "+":
                    continue

                # Check if new position is on the border
                is_exit = (
                    new_row == 0 or
                    new_row == rows - 1 or
                    new_col == 0 or
                    new_col == cols - 1
                )

                # If it is an exit, return steps + 1
                if is_exit:
                    return steps + 1

                # Mark cell as visited
                maze[new_row][new_col] = "+"

                # Add cell to queue
                queue.append((new_row, new_col, steps + 1))

        # If no exit found
        return -1
        