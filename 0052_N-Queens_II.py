class Solution:
    def totalNQueens(self, n: int) -> int:
        '''Time O(n!) Space O(n)'''
        def is_not_under_attack(row, col, cols, hills, dales):
            return not (cols[col] or hills[row + col] or dales[row - col])
        
        def place_queen(row, col, cols, hills, dales):
            cols[col] = 1
            hills[row + col] = 1
            dales[row - col] = 1
        
        def remove_queen(row, col, cols, hills, dales):
            cols[col] = 0
            hills[row + col] = 0
            dales[row - col] = 0
        
        def n_queens(row, cols, hills, dales, count):
            if row == n:
                return count + 1
            for col in range(n):
                if is_not_under_attack(row, col, cols, hills, dales):
                    place_queen(row, col, cols, hills, dales)
                    count = n_queens(row + 1, cols, hills, dales, count)
                    remove_queen(row, col, cols, hills, dales)
            return count
        
        cols = [0] * n # only need to check if the col empty since we are traversing rows
        hills = [0] * (2 * n + 1)
        dales = [0] * (2 * n + 1)
        return n_queens(0, cols, hills, dales, 0)