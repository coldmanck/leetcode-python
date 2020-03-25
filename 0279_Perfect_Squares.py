# Runtime: 6004 ms, faster than 12.43% of Python3 online submissions for Perfect Squares.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Perfect Squares.

import math
class Solution:
    def numSquares(self, n: int) -> int:
        greatest_square_number = int(math.sqrt(n))
        perfect_numbers = [i**2 for i in range(1, greatest_square_number + 1)]
        # table = [[-1] * (n + 1) for _ in range(len(perfect_numbers))]
        # table[0] = [i for i in range(n + 1)]
        table = [i for i in range(n + 1)]
        for i in range(1, len(perfect_numbers)):
            for j in range(n + 1):
                # table[i][j] = min(table[i-1][j], table[i][j-perfect_numbers[i]] + 1) if j >= perfect_numbers[i] else table[i-1][j]
                table[j] = min(table[j], table[j-perfect_numbers[i]] + 1) if j >= perfect_numbers[i] else table[j]
        
        # return table[-1][-1]
        return table[-1]