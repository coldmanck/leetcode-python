# Runtime: 32 ms, faster than 57.55% of Python3 online submissions for Game of Life.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Game of Life.

import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_nb_of_live_neighbor(board, i, j):
            left = max(j-1, 0)
            right = min(j+1, len(board[0])-1)
            up = max(i-1, 0)
            down = min(i+1, len(board)-1)
            nb = 0
            for k in range(up, down + 1):
                for l in range(left, right + 1):
                    if k == i and l == j: continue
                    nb += board[k][l]
                    # if board[k][l] == 1 or board[k][l] == -1:
                    #     nb += 1
            return nb
        
        board_old = copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                nb_of_live_neighbor = get_nb_of_live_neighbor(board_old, i, j)
                if board[i][j] == 0 and nb_of_live_neighbor == 3:
                    board[i][j] = 1 # 2 # from 0 to 1
                else:
                    if nb_of_live_neighbor < 2 or nb_of_live_neighbor > 3:
                        board[i][j] = 0 # -1 # from 1 to 0
        
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] == 2:
        #             board[i][j] = 1
        #         elif board[i][j] == -1:
        #             board[i][j] = 0