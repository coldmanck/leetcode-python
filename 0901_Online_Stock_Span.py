class StockSpanner:

    def __init__(self):
        self.data = [] # stack

    def next(self, price: int) -> int:
        # stack time O(n) space O(n) in worst case
        cur_span = 1
        while self.data and price >= self.data[-1][0]:
            _, span = self.data.pop()
            cur_span += span
        self.data.append((price, cur_span))
        return cur_span
        
        # brute-force O(n^2)
        # self.data.append(price)
        # i = len(self.data) - 1
        # ans = 0
        # while i >= 0 and self.data[i] <= price:
        #     ans += 1
        #     i -= 1
        # return ans
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)