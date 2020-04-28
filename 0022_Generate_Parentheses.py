# Runtime: 32 ms, faster than 70.43% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 13.1 MB, less than 91.11% of Python3 online submissions for Generate Parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''Time = Space complexity = n-th Catalan number = 1/(n+1) * C^{2n}_n'''

        '''Recursion'''
        # def backtrack(ans, cur_ans='', n_left=0, n_right=0):
        #     if len(cur_ans) == 2 * n:
        #         ans.append(cur_ans)
        #         return
        #     if n_left < n:
        #         backtrack(ans, cur_ans + '(', n_left + 1, n_right)
        #     if n_right < n_left:
        #         backtrack(ans, cur_ans + ')', n_left, n_right + 1)
        
        # ans = []
        # backtrack(ans)
        # return ans

        '''Iterative solution (DFS)'''
        if n == 0:
            return []
        stack = [('(', 1, 0)]
        ans = []
        while stack:
            cur_ans, n_left, n_right = stack.pop()
            if len(cur_ans) == 2 * n:
                ans.append(cur_ans)
                continue
            if n_left < n:
                stack.append((cur_ans + '(', n_left + 1, n_right))
            if n_right < n_left:
                stack.append((cur_ans + ')', n_left, n_right + 1))
        return ans