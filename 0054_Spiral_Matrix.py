class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''solution 0'''
        # if not matrix:
        #     return []
        # ans = []
        # n_row, n_col = len(matrix), len(matrix[0])
        # i = j = 0
        # oris = {(0, 1):(1, -1), (1, 0):(-1, -1), (0, -1):(-1, 1), (-1, 0):(1, 1)}
        # while True:
        #     for ori, ij_rev in oris.items():
        #         if len(ans) == n_row * n_col:
        #             return ans
        #         while i >= 0 and i < n_row and j >= 0 and j < n_col and matrix[i][j] != None:
        #             ans.append(matrix[i][j])
        #             matrix[i][j] = None
        #             i, j = i + ori[0], j + ori[1]
        #         i, j = i + ij_rev[0], j + ij_rev[1]

        '''solution 1: with auxiliary matrix O(n)'''
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # width, height = len(matrix[0]), len(matrix)
        # matrix_visited = [[False] * width for _ in range(height)]
        # count = 0
        # i = j = 0
        # ans = []
        # d_i = 0
        # while count < width * height:
        #     ans.append(matrix[i][j])
        #     matrix_visited[i][j] = True
        #     count += 1
        #     if count == width * height:
        #         break
            
        #     i_tmp = i + directions[d_i][0]
        #     j_tmp = j + directions[d_i][1] 
        #     while not (0 <= i_tmp < height and 0 <= j_tmp < width and not matrix_visited[i_tmp][j_tmp]):
        #         d_i = (d_i + 1) % len(directions)
        #         i_tmp = i + directions[d_i][0]
        #         j_tmp = j + directions[d_i][1] 
        #     i, j = i_tmp, j_tmp

        # return ans

        '''solution 2: using boundaries without auxiliary matrix'''
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        ans = []

        while top <= bottom and left <= right:
            # row right-ward
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1

            # col down-ward
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # row left-ward
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                # col up-ward
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
            
        return ans

                