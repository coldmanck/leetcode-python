# Runtime: 32 ms, faster than 38.95% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Number of 1 Bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        # return Counter(bin(n))['1'] # bin(n).count('1')

        count = 0
        while n:
            n &= n - 1
            count += 1
        return count