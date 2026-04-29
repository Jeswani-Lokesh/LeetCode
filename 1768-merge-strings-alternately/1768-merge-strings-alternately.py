class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # Pointer for word1
        i = 0

        # Pointer for word2
        j = 0

        # List to store result characters
        result = []

        # Loop until both strings are fully used
        while i < len(word1) or j < len(word2):

            # If word1 still has characters
            if i < len(word1):
                # Add character from word1
                result.append(word1[i])
                # Move pointer forward
                i += 1

            # If word2 still has characters
            if j < len(word2):
                # Add character from word2
                result.append(word2[j])
                # Move pointer forward
                j += 1

        # Join list into a string and return
        return "".join(result)