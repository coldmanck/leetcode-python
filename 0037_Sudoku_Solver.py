class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        Time: brute force O(9^{9*9}) = O(9^81) -> backtrack O(9!^9)
        Space: 
        '''
        def is_valid(i, j, val, board):
            start_row, start_col = (i // 3) * 3, (j // 3) * 3
            grid = [board[k][l] for k in range(start_row, start_row+3) for l in range(start_col, start_col+3)]
            return val not in board[i] and val not in [board[k][j] for k in range(len(board))] and val not in grid
        
        def find_next(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        return i, j
            return -1, -1

        def solve(board):
            row, col = find_next(board)
            if row == -1 and col == -1:
                return True
            print(f'Processing {row} {col}')
            for val in range(1, 10):
                if is_valid(row, col, str(val), board):
                    board[row][col] = str(val)
                    # import pdb; pdb.set_trace()
                    if solve(board):
                        return True
                    board[row][col] = '.'
            return False
        
        print(solve(board))
        print(board)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
sol.solveSudoku(board)