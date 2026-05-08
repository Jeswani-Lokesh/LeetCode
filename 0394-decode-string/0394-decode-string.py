class Solution:
    def decodeString(self, s: str) -> str:

        # Stack stores:
        # (previous_string, repeat_count)
        stack = []

        # Current number being formed
        current_num = 0

        # Current decoded string
        current_string = ""

        # Process each character
        for ch in s:

            # If character is a digit
            if ch.isdigit():

                # Build the full number
                current_num = current_num * 10 + int(ch)

            # If opening bracket
            elif ch == "[":

                # Save current state to stack
                stack.append((current_string, current_num))

                # Reset for new substring
                current_string = ""
                current_num = 0

            # If closing bracket
            elif ch == "]":

                # Get previous string and repeat count
                prev_string, num = stack.pop()

                # Decode current part
                current_string = prev_string + num * current_string

            # Normal character
            else:

                # Add character to current string
                current_string += ch

        # Final decoded string
        return current_string