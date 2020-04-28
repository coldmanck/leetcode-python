# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''All algos Time: O(n) Space: O(h) (=O(logn) if balanced otherwise O(n))'''
        
        '''recursive solution'''
        # if not p and not q:
        #     return True
        # if (not p or not q) or p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        '''iterative solution (DFS)'''
        # stack = [(p, q)]
        # while stack:
        #     p, q = stack.pop()
        #     if not p and not q:
        #         continue
        #     if (not p or not q) or p.val != q.val:
        #         return False
        #     stack.append((p.right, q.right))
        #     stack.append((p.left, q.left))
        # return True
    
        '''iterative solution (BFS)'''
        from collections import deque
        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if not p and not q:
                continue
            if (not p or not q) or p.val != q.val:
                return False
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
        return True
            
        