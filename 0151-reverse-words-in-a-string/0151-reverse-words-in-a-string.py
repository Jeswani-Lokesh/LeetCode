class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove extra spaces from beginning and end
        s = s.strip()
        
        # Split the string into individual words
        words = s.split()
        
        # Reverse the order of the words
        words = words[::-1]
        
        # Join the words back into a single string
        result = " ".join(words)
        
        # Return the final string
        return result
        