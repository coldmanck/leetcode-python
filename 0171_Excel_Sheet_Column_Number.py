# Runtime: 28 ms, faster than 79.27% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.

class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans = ans * 26 + ord(s[i]) - 64
        return ans