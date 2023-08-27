class Node:
    def __init__(self):
        self.children = {} # Dict[ch, Node]
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            cur = cur.children.setdefault(ch, Node())
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end
            if word[idx] == '.':
                for next_node in node.children.values():
                    if dfs(next_node, idx + 1):
                        return True
            return word[idx] in node.children and dfs(node.children[word[idx]], idx + 1)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)