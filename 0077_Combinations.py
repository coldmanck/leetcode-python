class Solution:
    '''Backtrack. Time: O(k*C^n_k) Space (C^n_k)'''
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, cur_arr, ans, arr):
            if len(cur_arr) == k:
                ans.append(cur_arr)
                return
            for j in range(i, n):
                backtrack(j + 1, cur_arr + [arr[j]], ans, arr)
        
        ans = []
        arr = [i for i in range(1, n + 1)]
        backtrack(0, [], ans, arr)
        return ans

'''
Algorithm

Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

Here is a backtrack function which takes a first integer to add and a current combination as arguments backtrack(first, curr).

If the current combination is done - add it to output.

Iterate over the integers from first to n.

Add integer i into the current combination curr.

Proceed to add more integers into the combination : backtrack(i + 1, curr).

Backtrack by removing i from curr.

'''