class Solution:
    def fib(self, N: int) -> int:
        # recursion with memoization (DP)
        # Time O(n) Space O(n)
        '''
        cache = {}
        
        def fib_helper(N):
            if N == 0 or N == 1:
                return N
            if N in cache:
                return cache[N]
            cache[N] = fib_helper(N - 1) + fib_helper(N - 2)
            return cache[N]
        
        return fib_helper(N)
        '''
        
        # Iterative solution
        # Time O(n) Space O(1)
        if N < 2: 
            return N
        prev, curr = 0, 1
        for i in range(2, N + 1):
            nextt = prev + curr
            prev, curr = curr, nextt
        return curr
            