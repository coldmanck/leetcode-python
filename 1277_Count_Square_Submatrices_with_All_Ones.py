class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''DP solution'''
        if not matrix:
            return 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dp[0] = matrix[0]
        ans = sum(dp[0])
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    if j == 0:
                        dp[i][j] = matrix[i][j]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ans += dp[i][j]
        return ans
        
        '''BFS solution'''
        # queue = []
        # ans = 0
        # directions = ((1, 0), (0, 1), (1, 1))
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 1:
        #             queue.append((i, j))
        #             while queue:
        #                 ans += 1
        #                 temp = []
        #                 visited = set()
        #                 is_valid = True
        #                 for i2, j2 in queue:
        #                     for ii, jj in directions:
        #                         i3, j3 = i2 + ii, j2 + jj
        #                         if not (0 <= i3 < len(matrix) and 0 <= j3 < len(matrix[0])) or matrix[i3][j3] != 1:
        #                             is_valid = False
        #                             break
        #                         else:
        #                             if (i3, j3) not in visited:
        #                                 visited.add((i3, j3))
        #                                 temp.append((i3, j3))
        #                     if not is_valid:
        #                         temp = []
        #                         break
        #                 queue = temp
        # return ans
                        