# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Iteration
        if isBadVersion(1):
            return 1
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
        # Recursion
        '''
        if isBadVersion(1):
            return 1
        
        def binary_search(n, left, right): # return first_bad_version
            mid = (left + right) // 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            return binary_search(n, left, mid - 1) if isBadVersion(mid) else binary_search(n, mid + 1, right)
        return binary_search(n, 1, n)
        '''