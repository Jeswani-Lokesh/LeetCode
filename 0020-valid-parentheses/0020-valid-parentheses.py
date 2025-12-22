class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map opening to corresponding closing brackets
        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []  # Stack to hold expected closing brackets

        for char in s:
            if char in bracket_map:
                # It's an opening bracket → push expected closing
                stack.append(bracket_map[char])
            else:
                # It's a closing bracket
                if not stack or stack[-1] != char:
                    return False  # Either unmatched or wrong order
                stack.pop()  # Matched correctly, pop from stack

        # If stack is empty, all brackets matched correctly
        return not stack