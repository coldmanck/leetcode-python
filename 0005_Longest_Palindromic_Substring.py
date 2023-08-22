class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start_idx = 0
        max_length = 1

        # initialize max_length=1 case
        for i in range(n):
            dp[i][i] = True

        # check length=2 strings
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start_idx = i
                max_length = 2

        # check length>=3 strings
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_length:
                        start_idx = i
                        max_length = length
            
        return s[start_idx:start_idx + max_length]
        # time = space = O(n^2)

