class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, cur_ans):
            if idx == len(nums):
                ans.append(cur_ans)
                return
            backtrack(idx + 1, cur_ans) # without nums[j]
            backtrack(idx + 1, cur_ans + [nums[idx]]) # with nums[j]
        ans = []
        backtrack(0, [])
        return ans