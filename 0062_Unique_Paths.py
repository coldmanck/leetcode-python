class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''Method 1: factorial with memoization. Time O(n) space (n)'''
        # cache = {}
        # def fact(i):
        #     if i <= 1:
        #         return 1
        #     if i not in cache:
        #         cache[i] = i * fact(i - 1)
        #     return cache[i]
        # return fact(m + n - 2) // (fact(m - 1) * fact(n - 1))
        
        '''Method 2: DP. Time O(m*n) space O(n)'''
        cache = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cache[j] += cache[j - 1]
        return cache[-1]
        