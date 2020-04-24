# Time Submitted
# Status
# Runtime
# Memory
# Language
# 2 minutes ago	Accepted	32 ms	13.9 MB	python3

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # DP (recursion with memoization) 
        # Time O(logn) Space O(logn)
        cache = {}
        if n < 0:
            x = 1/x
            n = -n
        def my_pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n not in cache:
                cache[x] = my_pow(x, n // 2) ** 2
                if n % 2:
                    cache[x] *= x
            return cache[x]
        return my_pow(x, n)