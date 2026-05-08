class Solution:
    def removeStars(self, s: str) -> str:

        # Stack to store characters
        stack = []

        # Go through each character
        for ch in s:

            # If character is a star
            if ch == "*":

                # Remove last character from stack
                stack.pop()

            else:
                # Otherwise add character to stack
                stack.append(ch)

        # Join stack into final string
        return "".join(stack)