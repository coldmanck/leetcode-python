class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking without duplicate solution (e.g. [1,7] and [7,1])
        # with sorting
        def backtrack(cur_ans, cur_sum, cand_idx):
            if cur_sum >= target:
                if cur_sum == target:
                    ans.append(cur_ans)
                return
            i = cand_idx
            while i < len(candidates):
                backtrack(cur_ans + [candidates[i]], cur_sum + candidates[i], i + 1)
                i += 1
                while i < len(candidates) and candidates[i] == candidates[i - 1]:
                    i += 1
        ans = []
        candidates.sort()
        backtrack([], 0, 0)
        return ans

        # Solution 2: backtracking without sorting
        '''
        ans = set()
        def helper(i, cur_ans):
            cur_sum = sum(cur_ans)
            if cur_sum == target:
                ans.add(tuple(sorted(cur_ans)))
                return
            if cur_sum > target or i >= len(candidates):
                return
            while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                i += 1
            if i == len(candidates) - 1:
                return
            helper(i + 1, cur_ans + [candidates[i]])
            helper(i + 1, cur_ans)
                
        helper(0, [])
        return list(ans)
        '''

        # backtracking with duplicate solution (e.g. [1,7] and [7,1])
        # def backtrack(cur_ans, cur_sum, candidates):
        #     if cur_sum >= target:
        #         if cur_sum == target:
        #             ans.append(cur_ans)
        #         return
        #     for i in range(len(candidates)):
        #         backtrack(cur_ans + [candidates[i]], cur_sum + candidates[i], candidates[:i] + candidates[i + 1:])
        # ans = []
        # backtrack([], 0, candidates)
        # return ans