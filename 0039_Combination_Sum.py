class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Runtime: 106 ms, faster than 56.94% of Python3 online submissions for Combination Sum.
        # Memory Usage: 13.9 MB, less than 61.13% of Python3 online submissions for Combination Sum.
        # Let N be the number of candidates, T be the target value, and M be the minimal value among the candidates.
        # time complexity: O(N^(T/M + 1)) (number of nodes in n-ary tree of height T/M)
        # space compleixty: O(T/M) for recursion function call stack
        ans = []
        def helper(i, cur_ans):
            cur_sum = sum(cur_ans)
            if cur_sum == target:
                ans.append(cur_ans)
                return
            if cur_sum > target or i >= len(candidates):
                return
            helper(i, cur_ans + [candidates[i]])
            helper(i + 1, cur_ans)
        helper(0, [])
        return ans

        '''backtrack'''
        def combination_sum(cur_ans, cur_sum, cand_idx):
            if cur_sum >= target:
                if cur_sum == target:
                    ans.append(cur_ans)
                return
            for i in range(cand_idx, len(candidates)):
                combination_sum(cur_ans + [candidates[i]], cur_sum + candidates[i], i)
        
        ans = []
        combination_sum([], 0, 0)
        return ans
        
        '''BFS'''
        # from collections import deque
        # queue = deque() # [cur_target, cur_ans]
        # queue.append((target, [], 0))
        # ans = []
        # while queue:
        #     cur_target, cur_ans, cand_idx = queue.popleft()
        #     for i in range(cand_idx, len(candidates)):
        #         new_target = cur_target - candidates[i]
        #         if new_target == 0:
        #             ans.append(cur_ans + [candidates[i]])
        #         elif new_target > 0:
        #             queue.append((cur_target - candidates[i], cur_ans + [candidates[i]], i))
        # return ans