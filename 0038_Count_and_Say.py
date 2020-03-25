# Easy
# Runtime: 32 ms, faster than 73.01% of Python3 online submissions for Count and Say.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Count and Say.

class Solution:
    def countAndSay(self, n: int) -> str:
        def count_and_say(n):
            if n == 1:
                return '1'
            
            cur_s = ''
            idx = 0
            cur_sum = 0
            s = count_and_say(n - 1)
            for i, ch in enumerate(s):
                if ch != s[idx]:
                    cur_s += str(cur_sum) + s[idx]
                    cur_sum = 1
                    idx = i
                else:
                    cur_sum += 1
            cur_s += str(cur_sum) + s[idx]
            return cur_s
        
        return count_and_say(n)