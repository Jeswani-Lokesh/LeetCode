class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store Roman numerals and their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # Final result
        prev_value = 0  # Track previous value for subtraction cases

        # Traverse the string from right to left
        for char in reversed(s):
            curr_value = roman_map[char]  # Get the integer value of the Roman symbol

            if curr_value < prev_value:
                # Subtractive case: e.g., I before V (IV = 4)
                total -= curr_value
            else:
                # Normal addition case
                total += curr_value

            # Update the previous value for next iteration
            prev_value = curr_value

        return total  # Return the final computed value
