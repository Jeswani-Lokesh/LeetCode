class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by "/"
        parts = path.split("/")

        # Stack to store valid folder names
        stack = []

        # Go through each part of the split path
        for part in parts:
            # Ignore empty strings and current directory "."
            if part == "" or part == ".":
                continue

            # If part is "..", go back one directory if possible
            elif part == "..":
                if stack:
                    stack.pop()

            # Otherwise, it is a valid folder name
            else:
                stack.append(part)

        # Join the stack with "/" and add leading "/"
        return "/" + "/".join(stack)