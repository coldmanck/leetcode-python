# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        # method 1: transform to inorder traversal array and maintain a current index
        # time: O(n) __init__, O(1) next() and hasNext()
        # space O(n)
        '''
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
            
        self.data = inorder(root)
        self.idx = -1
        '''
        # method 2: follow iterative inorder traversal solution
        # time: next O(h)? others O(1)
        # space: O(h)
        self.root = root
        self.stack = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        '''
        self.idx += 1
        return self.data[self.idx]
        '''
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        self.root = self.stack.pop()
        ans = self.root.val
        self.root = self.root.right
        return ans

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        '''
        return True if self.idx + 1 < len(self.data) else False
        '''
        return self.root or self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()