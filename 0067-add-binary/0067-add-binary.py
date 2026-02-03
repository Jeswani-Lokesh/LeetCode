class Solution:
    def addBinary(self, a: str, b: str) -> str:
         # Convert binary string a to an integer
        num1 = int(a, 2)

        # Convert binary string b to an integer
        num2 = int(b, 2)

        # Add the two integers
        total = num1 + num2

        # Convert the sum back to binary
        # bin() gives something like '0b101'
        binary_result = bin(total)

        # Remove the '0b' part and return only the binary number
        return binary_result[2:]
        