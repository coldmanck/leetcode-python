# Runtime: 28 ms, faster than 67.93% of Python3 online submissions for Unique Binary Search Trees.
# Memory Usage: 13.9 MB, less than 10.71% of Python3 online submissions for Unique Binary Search Trees.

class Solution:
    def numTrees(self, n: int) -> int:
        '''Recursion with memoization
        Time: O(n^2)
        Space: O(n)
        '''
        cache = {}
        
        def num_trees(n):
            if n == 0:
                return 1
            if n not in cache:
                cache[n] = 0
                for i in range(1, n + 1):
                    cache[n] += (num_trees(i - 1) * num_trees(n - i)) # this step costs O(n^2)
            return cache[n]
        
        return num_trees(n)