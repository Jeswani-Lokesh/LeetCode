class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If input is empty, return empty list
        if digits == "":
            return []

        # Map each digit to its letters
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # List to store final combinations
        result = []

        # Backtracking helper function
        def backtrack(index, current):
            # If current combination length equals digits length
            if index == len(digits):
                # Add complete combination to result
                result.append(current)

                # Stop this path
                return

            # Get current digit
            digit = digits[index]

            # Get letters for current digit
            letters = digit_to_letters[digit]

            # Try every letter for this digit
            for letter in letters:
                # Add letter and move to next digit
                backtrack(index + 1, current + letter)

        # Start from index 0 with empty string
        backtrack(0, "")

        # Return all combinations
        return result
        