# Time O(1) Space O(1)

class Solution:
    def findComplement(self, num: int) -> int:
        # bit mask (1)
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return mask ^ num
        
        # bit mask (2)
        # from math import log2
        # n = int(log2(num)) + 1
        # mask = 2 ** n - 1
        # return mask ^ num
        
        # ans = ['0b']
        # for ch in bin(num)[1:]:
        #     ans.append('1' if ch == '0' else '0')
        # return int(''.join(ans), 2)