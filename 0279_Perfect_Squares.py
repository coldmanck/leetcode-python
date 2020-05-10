class Solution:
    def numSquares(self, n: int) -> int:
        '''Lagrange's four-square theorem: 
        states that every natural number can be represented as the sum of four integer squares.
        Therefore the complexity is O(sqrt(n) ^ 4) = O(n^2)
        '''
        
        '''BFS'''
        largest_perfect_nb = int(math.sqrt(n))
        perfect_nbs = [i ** 2 for i in range(1, largest_perfect_nb + 1)]
        from collections import deque
        queue = deque()
        queue.append((n, 0))
        while queue:
            n, count = queue.popleft()
            for nb in perfect_nbs:
                new_n = n - nb
                if new_n == 0:
                    return count + 1
                if new_n > 0:
                    queue.append((new_n, count + 1))
        
        '''DP'''
        # import math
        # largest_perfect_nb = int(math.sqrt(n))
        # cache = [i for i in range(n + 1)]
        # for i in range(1, largest_perfect_nb + 1):
        #     nb = i ** 2
        #     for j in range(1, n + 1):
        #         cache[j] = min(cache[j], cache[j - nb] + 1) if j >= nb else cache[j]
        # return cache[-1]