class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # key: sorted tuple → value: list of words

        for word in strs:
            # Sort the word and use tuple of chars as hashable key
            key = tuple(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())  # return grouped anagrams
        