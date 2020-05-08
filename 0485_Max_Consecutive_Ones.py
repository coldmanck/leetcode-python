class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_count = max_count = 0
        for num in nums:
            if num == 1:
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                cur_count = 0
        return max_count