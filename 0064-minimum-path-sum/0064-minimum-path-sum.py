class Solution:
    def minPathSum(self, grid: List[List[int]]):
        # Get grid dimensions
        m, n = len(grid), len(grid[0])
        
        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                # Skip the starting cell
                if i == 0 and j == 0:
                    continue
                # If in the first row, can only come from the left
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                # If in the first column, can only come from above
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                # Otherwise, take the minimum path from left or above
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        # The answer is in the bottom-right cell
        return grid[-1][-1]
        