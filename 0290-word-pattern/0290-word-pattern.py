class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        return list(map(pattern.index, pattern)) == list(map(words.index, words))
        