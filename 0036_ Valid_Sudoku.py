# Runtime: 104 ms, faster than 33.15% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Valid Sudoku.

from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_if_row_valid(row):
            c = Counter(row)
            del c['.']
            if any([v > 1 for v in list(c.values())]):
                return False
            return True
        
        for row in board:
            if not check_if_row_valid(row):
                return False
        for col_num in range(len(board)):
            row = [board[i][col_num] for i in range(len(board))]
            if not check_if_row_valid(row):
                return False
        for row_num in range(len(board)//3):
            for col_num in range(len(board)//3):
                left, top = col_num*3, row_num*3
                row = [board[left+i][top+j] for i in range(3) for j in range(3)]
                if not check_if_row_valid(row):
                    return False
        return True