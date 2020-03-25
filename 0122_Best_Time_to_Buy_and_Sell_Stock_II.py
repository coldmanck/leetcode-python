# Runtime: 48 ms, faster than 99.69% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 13.8 MB, less than 87.81% of Python3 online submissions for Best Time to Buy and Sell Stock II.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += (prices[i + 1] - prices[i])
        return profit