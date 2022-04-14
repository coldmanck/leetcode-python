class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Runtime: 37 ms, faster than 94.48% of Python3 online submissions for Permutations.
        # Memory Usage: 14.1 MB, less than 61.08% of Python3 online submissions for Permutations.
        ans = []
        def helper(i, cur_ans, cur_ans_set): # cur_ans_set for O(1) look-up
            if i == len(nums):
                ans.append(cur_ans[:])
                return
            for j in range(len(nums)):
                if nums[j] not in cur_ans_set:
                    cur_ans_set.add(nums[j])
                    helper(i + 1, cur_ans + [nums[j]], cur_ans_set)
                    cur_ans_set.remove(nums[j])
        helper(0, [], set())
        return ans
        
        # Runtime: 40 ms, faster than 57.02% of Python3 online submissions for Permutations.
        # Memory Usage: 13 MB, less than 96.43% of Python3 online submissions for Permutations.
        '''
        def permute_helper(i, ans): # i means currently working on nums[i:]
            if i == len(nums) - 1:
                ans.append(nums.copy())
                return
            for j in range(i, len(nums)):  # j means starting from diff element
                nums[i], nums[j] = nums[j], nums[i]
                permute_helper(i + 1, ans)
                nums[i], nums[j] = nums[j], nums[i]
        ans = []
        permute_helper(0, ans)
        return ans
        '''