class Solution:
    def intToRoman(self, num: int) -> str:
        # List of values and their Roman symbols
        values = [1000, 900, 500, 400, 100, 90, 50, 40,
                  10, 9, 5, 4, 1]

        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]

        # Store the final Roman numeral
        result = ""

        # Go through each value
        for i in range(len(values)):
            
            # While the number is greater than or equal to the value
            while num >= values[i]:
                
                # Add the corresponding Roman symbol
                result += symbols[i]

                # Subtract the value from num
                num -= values[i]

        # Return the final Roman number
        return result
        