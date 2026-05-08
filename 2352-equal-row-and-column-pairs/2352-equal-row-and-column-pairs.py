class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # Dictionary to count rows
        row_count = {}

        # Step 1:
        # Store every row as a tuple in dictionary
        for row in grid:

            # Convert row to tuple (lists cannot be dictionary keys)
            row_tuple = tuple(row)

            # Count occurrences of this row
            row_count[row_tuple] = row_count.get(row_tuple, 0) + 1

        # This stores final answer
        pairs = 0

        n = len(grid)

        # Step 2:
        # Build each column
        for col in range(n):

            # Create current column
            current_col = []

            for row in range(n):
                current_col.append(grid[row][col])

            # Convert column to tuple
            col_tuple = tuple(current_col)

            # If this column exists as a row
            if col_tuple in row_count:

                # Add its frequency
                pairs += row_count[col_tuple]

        # Return total pairs
        return pairs
        