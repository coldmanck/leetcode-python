class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time complexity is O(N^target) where N is a length of candidates array.
        # Space complexity is O(target).

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