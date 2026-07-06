class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Result list
        result = []

        # Initialize boundaries
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        # Continue until boundaries cross
        while top <= bottom and left <= right:

            # Traverse left -> right
            for col in range(left, right + 1):
                result.append(matrix[top][col])

            top += 1

            # Traverse top -> bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])

            right -= 1

            # Traverse right -> left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])

                bottom -= 1

            # Traverse bottom -> top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])

                left += 1

        return result
        