# Runtime: 272 ms, faster than 17.14% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 34.7 MB, less than 7.41% of Python3 online submissions for Implement Trie (Prefix Tree).

class Node:
    def __init__(self, ch=None):
        self.ch = ch
        self.children = [None] * 27

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        idx = 0
        node = self.root
        while idx < len(word) and node.children[ord(word[idx]) - ord('a')]:
            node = node.children[ord(word[idx]) - ord('a')]
            idx += 1
        while idx < len(word):
            node.children[ord(word[idx]) - ord('a')] = Node(word[idx])
            node = node.children[ord(word[idx]) - ord('a')]
            idx += 1
        node.children[-1] = Node('END')
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        idx = 0
        node = self.root
        while idx < len(word) and node.children[ord(word[idx]) - ord('a')]:
            node = node.children[ord(word[idx]) - ord('a')]
            idx += 1
        return True if idx == len(word) and node.children[-1] and node.children[-1].ch == 'END' else False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        idx = 0
        node = self.root
        while idx < len(prefix) and node.children[ord(prefix[idx]) - ord('a')]:
            node = node.children[ord(prefix[idx]) - ord('a')]
            idx += 1
        return True if idx == len(prefix) else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)