import random
class Solution:

    def __init__(self, w: List[int]):
        # self.w = []
        # for i in range(len(w)):
        #     self.w.extend([i] * w[i])

        '''Construct normalized accumulated array: O(len(w))'''
        self.w = []
        s, cum = sum(w), 0
        for i in range(len(w)):
            cum += w[i] / s
            self.w.append(cum)

    def pickIndex(self) -> int:
        # return random.choice(self.w)

        '''random sample a number and binary search: O(log(len(w)))'''
        choice = random.random()
        left, right = 0, len(self.w)
        while left < right:
            mid = (left + right) // 2
            if self.w[mid] < choice:
                left = mid + 1
            else:
                right = mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()