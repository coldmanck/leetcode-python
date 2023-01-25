# Runtime: 96 ms, faster than 25.84% of Python3 online submissions for Single Number.
# Memory Usage: 15.1 MB, less than 18.03% of Python3 online submissions for Single Number.

from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n) time O(n) space
        '''
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        for k, v in counter.items():
            if v == 1:
                return k
        '''

        # O(n) time O(1) space
        xor = 0
        for num in nums:
            xor ^= num
        return xor