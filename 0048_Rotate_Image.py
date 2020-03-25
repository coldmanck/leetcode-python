# Runtime: 32 ms, faster than 74.39% of Python3 online submissions for Rotate Image.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Rotate Image.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - n // 2):
                matrix[i][j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j]
                matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i]
                matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i] = matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]