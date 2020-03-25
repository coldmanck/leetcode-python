# Runtime: 32 ms, faster than 70.43% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 13.1 MB, less than 91.11% of Python3 online submissions for Generate Parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # ans_set = set()
        # def gen_par(i, left_arr, right_arr):
        #     if i == 1:
        #         ans_set.add(left_arr + '()' + right_arr)
        #         return
        #     # '(' + gen_par(i-1) + ')'
        #     gen_par(i-1, '(' + left_arr, right_arr + ')') 
        #     # gen_par(i-1) + '()'
        #     gen_par(i-1, left_arr, right_arr + '()')
        #     # '()' + gen_par(i-1) 
        #     gen_par(i-1, '()' + left_arr, right_arr)
        #     # gen_par(i-2) + gen_par(i-2)
        #     gen_par(i-2, '(' + left_arr + ')', '(' + right_arr + ')')
        # gen_par(n, '', '')
        # return list(ans_set)
        ans = []
        def backtrack(s, left, right):
            if len(s) == 2*n:
                ans.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        
        backtrack('', 0, 0)
        return ans