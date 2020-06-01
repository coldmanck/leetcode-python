class Solution:
    def mySqrt(self, x: int) -> int:
        '''time O(logn) space O(1)'''
        # if x <= 1:
        #     return x
        # left, right = 1, x // 2
        # while left < right:
        #     mid = (left + right) // 2
        #     if mid ** 2 < x:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return left - 1 if left ** 2 > x else left
        
        '''Newton's Method'''
        if x <= 1:
            return x
        guess = x // 2
        while True:
            guess2 = (guess + x / guess) / 2
            if int(guess) == int(guess2):
                return int(guess)
            guess = guess2