class Solution:
    def mySqrt(self, x: int) -> int:
        # time O(logn) space O(1)
        if x <= 1:
            return x
        
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            mid_square = mid ** 2
            if mid_square == x or (mid_square < x and (mid_square + 2 * mid + 1) > x):
                return mid
            if mid_square < x:
                left = mid + 1
            else:
                right = mid - 1