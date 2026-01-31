class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []

        # Dictionary to match closing brackets to opening brackets
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Loop through each character in the string
        for char in s:
            # If character is an opening bracket
            if char in matching.values():
                # Push it onto the stack
                stack.append(char)
            else:
                # If stack is empty, there is no opening bracket to match
                if not stack:
                    return False

                # Pop the last opening bracket
                top = stack.pop()

                # Check if it matches the current closing bracket
                if top != matching[char]:
                    return False

        # If stack is empty, all brackets matched correctly
        return len(stack) == 0
        