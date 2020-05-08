# Runtime: 272 ms, faster than 17.14% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 34.7 MB, less than 7.41% of Python3 online submissions for Implement Trie (Prefix Tree).

class Node:
    def __init__(self, ch=None):
        self.children = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
    def word_idx_in_children(self, word_idx):
        return ord(word_idx) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        idx = 0
        node = self.root
        while idx < len(word) and node.children[self.word_idx_in_children(word[idx])]:
            node = node.children[self.word_idx_in_children(word[idx])]
            idx += 1
        while idx < len(word):
            node.children[self.word_idx_in_children(word[idx])] = Node(word[idx])
            node = node.children[self.word_idx_in_children(word[idx])]
            idx += 1
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        idx = 0
        node = self.root
        while idx < len(word) and node.children[self.word_idx_in_children(word[idx])]:
            node = node.children[self.word_idx_in_children(word[idx])]
            idx += 1
        return True if idx == len(word) and node.is_end else False
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        idx = 0
        node = self.root
        while idx < len(prefix) and node.children[self.word_idx_in_children(prefix[idx])]:
            node = node.children[self.word_idx_in_children(prefix[idx])]
            idx += 1
        return True if idx == len(prefix) else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)