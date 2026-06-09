class TrieNode:
    def __init__(self):
        # Dictionary stores character -> TrieNode
        self.children = {}

        # True if a complete word ends at this node
        self.is_word = False


class Trie:

    def __init__(self):
        # Root node does not store any character
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from root
        current = self.root

        # Go through every character in word
        for ch in word:
            # If character does not exist, create a new node
            if ch not in current.children:
                current.children[ch] = TrieNode()

            # Move to the child node
            current = current.children[ch]

        # Mark the end of the word
        current.is_word = True

    def search(self, word: str) -> bool:
        # Start from root
        current = self.root

        # Go through every character in word
        for ch in word:
            # If character does not exist, word is missing
            if ch not in current.children:
                return False

            # Move to the child node
            current = current.children[ch]

        # Return True only if full word ends here
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        # Start from root
        current = self.root

        # Go through every character in prefix
        for ch in prefix:
            # If character does not exist, prefix is missing
            if ch not in current.children:
                return False

            # Move to child node
            current = current.children[ch]

        # If all prefix characters exist, return True
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)