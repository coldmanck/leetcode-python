class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, cur_ans):
            ans.append(cur_ans)
            for j in range(idx, len(nums)):
                if j > idx and nums[j] == nums[j - 1]:
                    continue
                backtrack(j + 1, cur_ans + [nums[j]])
        ans = []
        nums.sort()
        backtrack(0, [])
        return ans
        
        '''generate all n! and use hashset to record unique ones'''
        # def backtrack(idx, cur_ans):
        #     if idx == len(nums):
        #         ans.add(tuple(sorted(cur_ans)))
        #         return
        #     backtrack(idx + 1, cur_ans + [nums[idx]])
        #     backtrack(idx + 1, cur_ans)
        # ans = set()
        # backtrack(0, [])
        # return list(ans) 