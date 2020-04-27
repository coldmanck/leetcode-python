# Runtime: 132 ms, faster than 30.97% of Python3 online submissions for N-Queens.
# Memory Usage: 14.2 MB, less than 5.00% of Python3 online submissions for N-Queens.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''Time O(n!) Space O(n)'''
        def is_not_under_attack(row, ans, queens, hills, dales, col):
            return not (queens[col] != (-1, -1) or hills[row + col] or dales[row - col])
        
        def place_queen(row, queens, hills, dales, col):
            queens[col] = (row, col)
            hills[row + col] = 1
            dales[row - col] = 1
        
        def remove_queen(row, queens, hills, dales, col):
            queens[col] = (-1, -1)
            hills[row + col] = 0
            dales[row - col] = 0
        
        def n_queens(row, ans, queens, hills, dales):
            if row == n:
                cur_ans = ['' for _ in range(n)]
                for r, c in queens:
                    cur_ans[r] = '.' * c + 'Q' + '.' * (n - c - 1)
                ans.append(cur_ans)
            for col in range(n):
                if is_not_under_attack(row, ans, queens, hills, dales, col):
                    place_queen(row, queens, hills, dales, col)
                    n_queens(row + 1, ans, queens, hills, dales)
                    remove_queen(row, queens, hills, dales, col)
        
        queens = [(-1, -1) for _ in range(n)] # (row, col)
        hills = [0] * (2*n+1)
        dales = [0] * (2*n+1)
        ans = []
        n_queens(0, ans, queens, hills, dales)
        return ans