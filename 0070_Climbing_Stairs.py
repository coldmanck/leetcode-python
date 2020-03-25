# Runtime: 32 ms, faster than 12.84% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.9 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.

class Solution:
    def climbStairs(self, n: int) -> int:
        # cache = [-1] * (n+1)
        # def climb_stairs(n):
        #     if n <= 2:
        #         return n
        #     if cache[n] == -1:
        #         cache[n] = climb_stairs(n - 1) + climb_stairs(n - 2)
        #     return cache[n]
        # return climb_stairs(n)
        if n <= 2:
            return n
        cache = [-1] * (n + 1)
        cache[:3] = [0, 1, 2]
        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]