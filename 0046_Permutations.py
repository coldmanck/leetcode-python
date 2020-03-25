# Runtime: 40 ms, faster than 57.02% of Python3 online submissions for Permutations.
# Memory Usage: 13 MB, less than 96.43% of Python3 online submissions for Permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permute_helper(i): # i means currently working on nums[i:]
            if i == len(nums) - 1:
                ans.append(nums.copy())
                return
            for j in range(i, len(nums)):  # j means starting from diff element
                nums[i], nums[j] = nums[j], nums[i]
                permute_helper(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        permute_helper(0)
        return ans