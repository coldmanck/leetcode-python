# Runtime: 68 ms, faster than 35.96% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 13.8 MB, less than 96.55% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = float('inf')
        for price in prices:
            if price < min_so_far:
                min_so_far = price
            max_profit = max(max_profit, price - min_so_far)
        return max_profit