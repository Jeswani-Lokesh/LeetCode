class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # If lengths are different, impossible
        if len(word1) != len(word2):
            return False

        # Dictionary to count frequency of characters in word1
        count1 = {}

        # Dictionary to count frequency of characters in word2
        count2 = {}

        # Count characters in word1
        for ch in word1:
            count1[ch] = count1.get(ch, 0) + 1

        # Count characters in word2
        for ch in word2:
            count2[ch] = count2.get(ch, 0) + 1

        # Condition 1:
        # Both strings must contain same unique characters
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Condition 2:
        # Frequency patterns must match
        if sorted(count1.values()) != sorted(count2.values()):
            return False

        # Both conditions satisfied
        return True