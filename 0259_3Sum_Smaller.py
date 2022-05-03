class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        n_ans = 0
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    n_ans += (right - left)
                    left += 1
                else:
                    right -= 1
        return n_ans