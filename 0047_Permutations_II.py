class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # pre-sort + backtrack with skipping repeated elements
        def backtrack(cur_ans, nums):
            if len(nums) == 0:
                ans.append(cur_ans)
                return
            j = 0
            while j < len(nums):
                backtrack(cur_ans + [nums[j]], nums[:j] + nums[j + 1:])
                j += 1
                while j < len(nums) and nums[j] == nums[j - 1]:
                    j += 1
        nums.sort()
        ans = []
        backtrack([], nums)
        return ans
        
        '''Generate all n! combinations and use hash set to store unique results'''
        # def backtrack(idx):
        #     if idx == len(nums):
        #         ans.add(tuple(nums[:]))
        #         return
        #     for j in range(idx, len(nums)):
        #         nums[j], nums[idx] = nums[idx], nums[j]
        #         backtrack(idx + 1)
        #         nums[j], nums[idx] = nums[idx], nums[j]
        # ans = set()
        # backtrack(0)
        # return [list(i) for i in ans]