class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_list(arr):
            arr = [int(i) for i in arr if i != '.']
            return len(set(arr)) == len(arr) and all(1 <= i <= 9 for i in arr)
        for arr in board:
            if not check_list(arr):
                return False
        for j in range(len(board[0])):
            arr = [board[i][j] for i in range(len(board))]
            if not check_list(arr):
                return False
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                arr = [board[i2][j2] for i2 in range(i, i+3) for j2 in range(j, j+3)]
                if not check_list(arr):
                    return False
        return True