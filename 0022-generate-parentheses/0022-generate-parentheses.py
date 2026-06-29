class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Store all valid combinations
        result = []

        # Backtracking function
        def backtrack(current, open_count, close_count):

            # If string has 2*n characters, it is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we still have some left
            if open_count < n:
                backtrack(
                    current + "(",
                    open_count + 1,
                    close_count
                )

            # Add ')' only if it keeps the string valid
            if close_count < open_count:
                backtrack(
                    current + ")",
                    open_count,
                    close_count + 1
                )

        # Start with an empty string
        backtrack("", 0, 0)

        return result
        