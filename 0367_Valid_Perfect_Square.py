class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Newton's method
        # x' = (x + num/x) * 1/2
        if num <= 1:
            return True
        x = num // 2
        while x ** 2 > num:
            x = (x + num/x) // 2
        return x ** 2 == num
        
        # find out sqrt(num) and return if it's an integer
        # if num <= 1:
        #     return True
        # left, right = 1, num // 2
        # while left <= right:
        #     mid = (left + right) // 2
        #     mid_square = mid ** 2
        #     if mid_square == num:
        #         return True
        #     if mid_square < num:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return False