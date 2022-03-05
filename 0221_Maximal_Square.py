class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # find maximum -> use dp
        # dp(i, j) means the side length of the largest square whose bottom right corner is cell (i, j)
        # tmp = min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1))
        # dp(i, j) = tmp + 1 if matrix[i][j] == 1 else tmp
        # dp(0, 0) = 0 if matrix[0, 0] == 0 else 1, dp(0, i) = max(dp(0, i - 1), matrix[0, i])
        max_len = 0
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if int(matrix[i - 1][j - 1]) == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len ** 2