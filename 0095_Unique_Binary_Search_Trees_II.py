# Runtime: 64 ms, faster than 37.91% of Python3 online submissions for Unique Binary Search Trees II.
# Memory Usage: 15.4 MB, less than 6.67% of Python3 online submissions for Unique Binary Search Trees II.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def gen_trees(left, right):
            if left > right:
                return [None]
            cur_subtrees = []
            for i in range(left, right + 1): # pick up a root
                left_subtrees = gen_trees(left, i - 1) # all possible left subtrees if i is choosen to be a root
                right_subtrees = gen_trees(i + 1, right) # all possible right subtrees if i is choosen to be a root
                # connect left and right subtrees to the root i
                for j in left_subtrees:
                    for k in right_subtrees:
                        node = TreeNode(i)
                        node.left = j
                        node.right = k
                        cur_subtrees.append(node)
            return cur_subtrees
        return gen_trees(1, n) if n else []

'''
Approach 1: Recursion
First of all let's count how many trees do we have to construct. As you could check in this article, the number of possible BST is actually a Catalan number.

Let's follow the logic from the above article, this time not to count but to actually construct the trees.

Algorithm

Let's pick up number i out of the sequence 1 ..n and use it as the root of the current tree. Then there are i - 1 elements available for the construction of the left subtree and n - i elements available for the right subtree. As we already discussed that results in G(i - 1) different left subtrees and G(n - i) different right subtrees, where G is a Catalan number.

Now let's repeat the step above for the sequence 1 ... i - 1 to construct all left subtrees, and then for the sequence i + 1 ... n to construct all right subtrees.

This way we have a root i and two lists for the possible left and right subtrees. The final step is to loop over both lists to link left and right subtrees to the root.
'''