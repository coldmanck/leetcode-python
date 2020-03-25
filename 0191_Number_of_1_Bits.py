# Runtime: 32 ms, faster than 38.95% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Number of 1 Bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n &= (n-1)
        return count