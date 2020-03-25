# Runtime: 36 ms, faster than 31.17% of Python3 online submissions for Happy Number.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Happy Number.

class Solution:
    def isHappy(self, n: int) -> bool:
        '''Method 1: hash table O(n) space'''
#         hash_table = set()
#         def is_happy(n):
#             if n == 1:
#                 return True
#             if n in hash_table:
#                 return False
#             hash_table.add(n)
            
#             total = 0
#             while n != 0:
#                 total += (n % 10) ** 2
#                 n //= 10
#             return is_happy(total)
#         return is_happy(n)
    
        '''Method 2 Cycle detection O(1) space'''
        def is_happy(n):
            first = nextt(n)
            second = n
            while first != second:
                first = nextt(nextt(first))
                second = nextt(second)
            return True if first == 1 else False
        
        def nextt(n):
            total = 0
            while n != 0:
                total += (n % 10) ** 2
                n //= 10
            return total
        
        return is_happy(n)