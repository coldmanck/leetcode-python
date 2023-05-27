class Solution:
    def reverseBits(self, n: int) -> int:
        if n >= 0:
            start_idx = 2
            sign = 1
        else:
            start_idx = 3
            sign = -1
        leading_one_counts = 32 - len(bin(n)) + start_idx
        return int(bin(n)[start_idx:][::-1] + '0' * leading_one_counts, 2) * sign