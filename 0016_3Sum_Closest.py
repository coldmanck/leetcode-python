class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # find nums[i] + nums[j] + nums[k] ~= target
        # -> minimize abs(nums[i] + nums[j] + nums[k] - target)
        
        min_dist = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                cur_dist = abs(cur_sum - target)
                if cur_dist == 0:
                    return target
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    min_sum = cur_sum
                if cur_sum <= target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return min_sum