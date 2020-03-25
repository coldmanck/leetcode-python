# Runtime: 280 ms, faster than 64.79% of Python3 online submissions for 4Sum II.
# Memory Usage: 37.8 MB, less than 8.33% of Python3 online submissions for 4Sum II.

from collections import Counter
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter = Counter([i+j for i in A for j in B])
        return sum([counter[-i-j] for i in C for j in D])