class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans = []
        n_row, n_col = len(matrix), len(matrix[0])
        i = j = 0
        oris = {(0, 1):(1, -1), (1, 0):(-1, -1), (0, -1):(-1, 1), (-1, 0):(1, 1)}
        while True:
            for ori, ij_rev in oris.items():
                if len(ans) == n_row * n_col:
                    return ans
                while i >= 0 and i < n_row and j >= 0 and j < n_col and matrix[i][j] != None:
                    ans.append(matrix[i][j])
                    matrix[i][j] = None
                    i, j = i + ori[0], j + ori[1]
                i, j = i + ij_rev[0], j + ij_rev[1]

                