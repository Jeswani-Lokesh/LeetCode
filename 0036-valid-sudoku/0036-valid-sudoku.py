class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create a list of 9 sets for rows
        rows = [set() for _ in range(9)]

        # Create a list of 9 sets for columns
        cols = [set() for _ in range(9)]

        # Create a list of 9 sets for 3x3 boxes
        boxes = [set() for _ in range(9)]

        # Loop through every row
        for r in range(9):
            # Loop through every column
            for c in range(9):
                # Get the current cell value
                value = board[r][c]

                # Skip empty cells
                if value == ".":
                    continue

                # Find which 3x3 box this cell belongs to
                box_index = (r // 3) * 3 + (c // 3)

                # If value already exists in the row, board is invalid
                if value in rows[r]:
                    return False

                # If value already exists in the column, board is invalid
                if value in cols[c]:
                    return False

                # If value already exists in the box, board is invalid
                if value in boxes[box_index]:
                    return False

                # Add value to the row set
                rows[r].add(value)

                # Add value to the column set
                cols[c].add(value)

                # Add value to the box set
                boxes[box_index].add(value)

        # If no duplicates were found, board is valid
        return True
        